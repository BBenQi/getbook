FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN python setup.py install

CMD [ "python", "./main.py" ]
