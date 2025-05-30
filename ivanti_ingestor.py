import requests
from azure.storage.blob import BlobServiceClient
import json
import os
from datetime import datetime

# === Ivanti API Config ===
IVANTI_URL = "https://trainer.thinktanks.co.za/HEAT/api/odata/businessobject/incidents"
IVANTI_HEADERS = {
    "Authorization": "rest_api_key=YOUR_IVANTI_KEY",
    "Accept": "application/json"
}

# === Azure Blob Config ===
AZURE_CONNECTION_STRING = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
BLOB_CONTAINER = "ivanti-raw"

def fetch_ivanti_data():
    response = requests.get(IVANTI_URL, headers=IVANTI_HEADERS)
    response.raise_for_status()
    return response.json()

def upload_to_blob(data):
    blob_service = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service.get_container_client(BLOB_CONTAINER)

    filename = f"ivanti_{datetime.utcnow().isoformat(timespec='seconds')}.json"
    blob_client = container_client.get_blob_client(filename)

    blob_client.upload_blob(json.dumps(data, indent=2), overwrite=True)
    print(f"✅ Uploaded Ivanti data to blob as: {filename}")

if __name__ == "__main__":
    try:
        ivanti_data = fetch_ivanti_data()
        upload_to_blob(ivanti_data)
    except Exception as e:
        print(f"❌ Error occurred: {e}")
