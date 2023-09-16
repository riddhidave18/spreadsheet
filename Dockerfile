FROM python:3.9

RUN pip3 install pytest 
WORKDIR /app
ADD . /app

CMD ["pytest"]