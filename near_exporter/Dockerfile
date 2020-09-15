FROM python:3.9.0rc1-slim-buster

LABEL maintainer="avadon.90@gmail.com"

ADD collector.py /code/collector.py
ADD requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

WORKDIR /code
ENV PYTHONPATH '/code/'

CMD ["python" , "/code/collector.py"]