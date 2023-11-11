FROM ubuntu:latest
WORKDIR /usr/src/app

COPY ./app .

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y python3-pip

RUN pip install -U pip && \
    pip install openai && \
    pip install aiogram && \
    pip install requests

RUN git clone https://github.com/Slavunia13/Helpers.git

CMD ["python3", "main.py"]