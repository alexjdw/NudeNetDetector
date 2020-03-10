FROM python:3.7

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install tensorflow
RUN pip3 install nudenet
RUN pip3 install -r requirements.txt

COPY ./ ./
RUN pytest
CMD ["gunicorn", "--config", "var/gunicorn.config.py", "nudity_classifier.app:app"]
