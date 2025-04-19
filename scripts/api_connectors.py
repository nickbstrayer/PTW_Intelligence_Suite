import requests
import os

# Hardcoded keys or pull from environment if needed
SAM_API_KEY = "f2gGlBlN4L8Q9HzeXyHHTvvNwkvz3m7OIxhFMDhu"
DATA_GOV_KEY = "MTcYHhfTdFCtXwczxk3gEnS4tpuvumTbfxNtsf5I"

def fetch_sam_details(solicitation_number):
    url = "https://api.sam.gov/prod/opportunities/v2/search"

    params = {
        "api_key": SAM_API_KEY,
        "noticeId": solicitation_number,
        "limit": 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print("DEBUG:", data)  # Optional for debugging only

        if data.get("opportunities"):
            opp = data["opportunities"][0]
            return {
                "agency_name": opp.get("contractingOfficeName", ""),
                "title": opp.get("title", ""),
                "published_date": opp.get("datePosted", ""),
                "due_date": opp.get("responseDeadLine", ""),
                "competition": opp.get("typeOfSetAsideDescription", ""),
                "estimated_value": float(opp.get("estimatedDollarValue", 0.0) or 0.0),
                "set_aside": opp.get("typeOfSetAsideDescription", ""),
                "psc": opp.get("productOrServiceCode", ""),
                "naics": opp.get("naics", {}).get("code", ""),
                "pop": opp.get("placeOfPerformance", {}).get("countryCode", ""),
                "description": opp.get("description", "")
            }

    except Exception as e:
        print(f"SAM.gov fetch error: {e}")

    return {}

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
