FROM python:3

ENV TZ=Europe/Berlin
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY src .
COPY system/start.sh .

EXPOSE 10000
VOLUME [ "/data" ]

CMD [ "./start.sh"]