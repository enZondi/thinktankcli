# app/ivanti_client.py
import requests
import os

IVANTI_API_KEY = os.environ.get('IVANTI_API_KEY')

def fetch_ivanti_incidents():
    if not IVANTI_API_KEY:
        return {"error": "IVANTI_API_KEY environment variable is not set"}
    
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
