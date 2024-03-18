# Specifies base image and tag
FROM gcr.io/google.com/cloudsdktool/cloud-sdk:latest
USER root
WORKDIR /dbt
#WORKDIR /root

# Copies the trainer code to the docker image.
COPY . .
#COPY main.py /root/main.py
#COPy requirements.txt /root/requirements.txt
#COPY script.sh /root/script.sh

# Installs additional packages
RUN pip3 install -r requirements.txt 

#Execute the Application
#ENTRYPOINT ["python3", "pipeline-update.py"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
