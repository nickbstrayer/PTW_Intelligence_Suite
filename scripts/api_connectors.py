import requests
import os

# You can hardcode keys for now or pull them from environment variables
SAM_API_KEY = "f2gGlBlN4L8Q9HzeXyHHTvvNwkvz3m7OIxhFMDhu"
DATA_GOV_KEY = "MTcYHhfTdFCtXwczxk3gEnS4tpuvumTbfxNtsf5I"

def fetch_sam_details(solicitation_number):
    url = "https://api.sam.gov/prod/opportunities/v2/search"
    params = {
        "api_key": SAM_API_KEY,
        "q": solicitation_number,
        "limit": 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()

        if results.get("opportunities"):
            opp = results["opportunities"][0]
            return {
                "agency_name": opp.get("contractingOfficeName", ""),
                "title": opp.get("title", "")
            }
    except Exception as e:
        print(f"SAM.gov fetch error: {e}")
    return {"agency_name": "", "title": ""}

def fetch_contract_history(duns_or_uei):
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "filters": {
            "recipient_search_text": [duns_or_uei]
        },
        "fields": ["Award Amount", "Recipient Name", "Award ID", "Action Date"],
        "limit": 1
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            contract = data["results"][0]
            return {
                "historical_value": contract.get("Award Amount", 0.0)
            }
    except Exception as e:
        print(f"Data.gov fetch error: {e}")
    return {"historical_value": 0.0}
