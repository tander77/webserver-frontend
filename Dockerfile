FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV PORT 5000
ENV SECRET_KEY newthing
EXPOSE 5000
ENTRYPOINT ["python3", "demo.py"]