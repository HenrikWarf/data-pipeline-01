from datetime import datetime
import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_pipeline():

    print("Function Started")

    import subprocess

    result = subprocess.call(["/bin/sh", "./script.sh"])

    print("Function Completed")

    return("Done!") 

if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)