# base image
FROM python:3.9-slim

# create working dir
WORKDIR /app

# copy all files
COPY . /app

#install depedencies
RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]