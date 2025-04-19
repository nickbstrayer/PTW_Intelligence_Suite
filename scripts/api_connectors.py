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
        data = response.json()

        if data.get("opportunities"):
            opp = data["opportunities"][0]
            return {
                "agency_name": opp.get("contractingOfficeName", ""),
                "title": opp.get("title", ""),
                "published_date": opp.get("publishedDate", ""),
                "due_date": opp.get("responseDeadLine", ""),
                "competition": opp.get("typeOfSetAsideDescription", ""),
                "estimated_value": float(opp.get("award", {}).get("value", 0.0)),
                "set_aside": opp.get("typeOfSetAsideDescription", ""),
                "psc": opp.get("productOrServiceCode", ""),
                "naics": opp.get("naicsCodes", [{}])[0].get("code", ""),
                "pop": opp.get("placeOfPerformance", {}).get("city", "") + ", " +
                       opp.get("placeOfPerformance", {}).get("state", ""),
                "description": opp.get("description", "")
            }
    except Exception as e:
        print(f"SAM.gov fetch error: {e}")
    return {
        "agency_name": "",
        "title": "",
        "published_date": "",
        "due_date": "",
        "competition": "",
        "estimated_value": 0.0,
        "set_aside": "",
        "psc": "",
        "naics": "",
        "pop": "",
        "description": ""
    }
