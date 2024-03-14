from datetime import datetime
import os
import sys
from google.cloud import aiplatform
from google.cloud.aiplatform import gapic as aip

from flask import Flask

from dbt.cli.main import dbtRunner, dbtRunnerResult

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_pipeline():
    
    # initialize
    dbt = dbtRunner()

    # create CLI args as a list of strings
    cli_args_one = ["deps", "--profiles-dir"]
    cli_args_two = ["debug", "--target dev", "--profiles-dir ."]
    cli_args_three = ["debug", "--target prod", "--profiles-dir ."]
    cli_args_four = ["run", "--target prod", "--profiles-dir ."]
    cli_args_five = ["test",  "--data", "--target dev", "--profiles-dir ."]

    # run the command
    res_one: dbtRunnerResult = dbt.invoke(cli_args_one)
    # inspect the results
    for r in res_one.result:
        print(f"{r.node.name}: {r.status}")

    res_two: dbtRunnerResult = dbt.invoke(cli_args_two)
    # inspect the results
    for r in res_two.result:
        print(f"{r.node.name}: {r.status}")

    res_three: dbtRunnerResult = dbt.invoke(cli_args_three)
    # inspect the results
    for r in res_three.result:
        print(f"{r.node.name}: {r.status}")

    res_four: dbtRunnerResult = dbt.invoke(cli_args_four)
    # inspect the results
    for r in res_four.result:
        print(f"{r.node.name}: {r.status}")

    res_five: dbtRunnerResult = dbt.invoke(cli_args_five)
    # inspect the results
    for r in res_five.result:
        print(f"{r.node.name}: {r.status}")
     

if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)