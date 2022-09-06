# Dockerfile, Image, Container
FROM python:3.10

ADD rps.py /app/
ADD test.py /app/

RUN pip install pytest

CMD [ "python3", "/app/rps.py" ]