import json

import pytest
from flask import url_for

from nudity_classifier.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config["SERVER_NAME"] = "test_server"

    with app.test_client() as client:
        with app.app_context():
            yield client


def make_request(client_method, url, data=None):
    return client_method(url, data=json.dumps(data), content_type="application/json")


def test_detect_endpoint(client):
    data = {"image_url":"https://img.ohpolly.com/3sgFaA-7KLILpPNURR2MxDnKMx4=/fit-in/1800x/catalog/product/1/8/1847_cream_edit6-.jpg"}
    url = url_for("nudenet_classifier_from_url")
    r = make_request(client.post, url, data)

    assert r.status_code == 200
    assert len(r.json) > 0
    belly_box = r.json[0]
    assert belly_box["label"] == "BELLY"
    assert "box" in belly_box
    assert len(belly_box["box"]) == 4
    assert belly_box["score"] > .5


def test_hc_endpoint(client):
    url = url_for("health_check")
    r = make_request(client.get, url)

    assert r.json
