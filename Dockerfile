FROM ubuntu:latest
WORKDIR /usr/src/app

COPY ./app .

RUN sudo apt-get update && sudo apt-get install -y git && sudo apt-get install -y pip

RUN pip install -U pip && \
pip install openai && \
pip install aiogram && \
pip install asyncio && \
pip install logging && \
pip install requests 

RUN git clone 

CMD ["python", "test.py"]