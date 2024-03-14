# Specifies base image and tag
FROM gcr.io/google.com/cloudsdktool/cloud-sdk:latest
WORKDIR /root

# Copies the trainer code to the docker image.
COPY pipeline.py /root/pipeline.py
COPy requirements.txt /root/requirements.txt
COPY script.sh /root/script.sh

# Installs additional packages
RUN pip3 install -r requirements.txt 

#Execute the Application
#ENTRYPOINT ["python3", "pipeline-update.py"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app


# FROM golang:1.22 as builder
# WORKDIR /app
# COPY invoke.go ./
# RUN CGO_ENABLED=0 GOOS=linux go build -v -o server

# FROM ghcr.io/dbt-labs/dbt:1.7.8-bigquery1.7.5
# USER root
# WORKDIR /dbt
# COPY --from=builder /app/server ./
# COPY script.sh ./
# COPY . ./

# ENTRYPOINT "./server"