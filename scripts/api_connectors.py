import requests

# Replace with your actual key or use environment variable
SAM_API_KEY = "your_sam_api_key_here"

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

        opportunities = results.get("opportunities", [])
        if not opportunities:
            return {}

        opp = opportunities[0]

        return {
            "agency_name": opp.get("contractingOfficeName", ""),
            "title": opp.get("title", ""),
            "published_date": opp.get("publishedDate", ""),
            "due_date": opp.get("responseDeadLine", ""),
            "competition": opp.get("typeOfSetAsideDescription", ""),
            "estimated_value": opp.get("estimatedDollarValue", 0.0),
            "set_aside": opp.get("typeOfSetAside", ""),
            "psc": opp.get("productOrServiceCode", ""),
            "naics": opp.get("naicsCode", ""),
            "pop": opp.get("placeOfPerformance", {}).get("country", ""),
            "description": opp.get("description", "")
        }

    except Exception as e:
        print(f"Error fetching from SAM.gov: {e}")
        return {}
