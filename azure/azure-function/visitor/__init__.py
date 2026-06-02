import azure.functions as func
import json
from azure.cosmos import CosmosClient
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    endpoint = os.environ["COSMOS_ENDPOINT"]
    key = os.environ["COSMOS_KEY"]

    client = CosmosClient(endpoint, key)
    db = client.get_database_client("resume-db")
    container = db.get_container_client("visits")

    try:
        item = container.read_item(item="1", partition_key="1")
        item["count"] += 1
    except:
        item = {"id": "1", "count": 1}

    container.upsert_item(item)

    return func.HttpResponse(
        json.dumps({"count": item["count"]}),
        mimetype="application/json"
    )