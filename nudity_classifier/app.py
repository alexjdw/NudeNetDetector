import json
import os
import uuid
from datetime import datetime

import pydload

from flask import Flask, jsonify, request

import logging
from nudenet import NudeDetector

app = Flask(__name__)
detector = NudeDetector()


@app.route("/hc-ping", methods=["GET"])
def health_check():
    return jsonify({
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S%z (%Z)"),
        "message": "PONG",
    }), 200


@app.route("/detect", methods=["POST"])
def nudenet_classifier_from_url():
    """
    Accepts a post request with "image_url". Downloads the
    image and returns a rating.
    """
    logging.debug("processing request for: ", request.json)
    url = request.json.get("image_url")
    result = detect(url)
    for entry in result:
        for k, v in entry.items():
            if not isinstance(v, (list, tuple, int, str)):
                entry[k] = float(v)
    return jsonify(result), 200


def detect(url):
    path = os.path.join(os.getcwd(), str(uuid.uuid4()))
    dload_status = pydload.dload(url, path, timeout=2, max_time=3)

    if not dload_status:
        return json.dumps({"error": "File too large to download"})
    res = detector.detect(path)

    try:
        os.remove(path)
    except Exception as e:
        logging.error(f"Unable to remove stored image: {path}")

    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
