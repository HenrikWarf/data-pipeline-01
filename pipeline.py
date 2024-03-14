from datetime import datetime
import os
import sys
from google.cloud import aiplatform
from google.cloud.aiplatform import gapic as aip

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_pipeline():

    import subprocess

    result = subprocess.run(["/bin/sh", "script.sh"], shell=True, capture_output=True, text=True)

    print(result.stdout)
     

if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)