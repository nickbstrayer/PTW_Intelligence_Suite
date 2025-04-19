import requests
import os

SAM_API_KEY = os.getenv("SAM_API_KEY", "your-sam-api-key-here")
DATA_GOV_KEY = os.getenv("DATA_GOV_KEY", "your-data-gov-key-here")

def fetch_sam_details(solicitation_number):
    url = f"https://api.sam.gov/opportunities/v2/search"
    params = {
        "api_key": SAM_API_KEY,
        "noticeId": solicitation_number,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("opportunitiesData"):
            item = data["opportunitiesData"][0]
            return {
                "agency": item.get("contractingOfficeName", ""),
                "title": item.get("title", "")
            }
        else:
            return {"agency": "", "title": ""}

    except Exception as e:
        print(f"SAM.gov API error: {e}")
        return {"agency": "", "title": ""}


def fetch_contract_history(agency_name):
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    headers = {"Content-Type": "application/json"}
    body = {
        "filters": {
            "agencies": [{"name": agency_name}]
        },
        "fields": ["Award Amount", "Recipient Name", "Awarding Agency", "Action Date"],
        "limit": 1
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        result = response.json()
        if result["results"]:
            return result["results"][0]
        return {}

    except Exception as e:
        print(f"Data.gov API error: {e}")
        return {}
