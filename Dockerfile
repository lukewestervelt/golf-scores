FROM python:3.9-slim-bullseye

WORKDIR /usr/src

# Setup flask environment
# https://docs.docker.com/compose/gettingstarted/#step-2-create-a-dockerfile
# ENV FLASK_APP=src/app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 5000

COPY ./src ./data
COPY ./data ./data

CMD ["flask", "run", "-h", "0.0.0.0"]
