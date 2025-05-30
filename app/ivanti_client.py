# app/ivanti_client.py
import requests
from config import IVANTI_API_KEY

def fetch_ivanti_incidents():
    url = "https://trainer.thinktanks.co.za/HEAT/api/odata/businessobject/incidents"
    headers = {
        "Authorization": f"rest_api_key={IVANTI_API_KEY}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
