FROM python:3.6.3
WORKDIR /usr/src/app

COPY install.txt install.txt

RUN pip install --upgrade pip
RUN pip install -r install.txt

COPY . .

RUN useradd -ms /bin/bash carpark
USER carpark

EXPOSE 8082

ENTRYPOINT ["python3", "index.py"]