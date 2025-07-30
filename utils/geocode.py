import requests

def geocode_postcode(postcode):
    """
    Geocodes a postcode to latitude and longitude using the Postcodes.io API.

    Parameters:
        postcode (str): The postcode to geocode.

    Returns:
        tuple: A tuple containing the latitude and longitude of the postcode, or None if geocoding fails.
    """
    postcode= postcode.replace(" ","")
    url = f"https://api.postcodes.io/postcodes/{postcode.strip()}"
    try:
        res = requests.get(url,timeout=5,verify=False)
        if res.status_code == 200:
            data = res.json()
            result = data["result"]
            return result['latitude'], result['longitude']
    except:
        pass
    return None, None
    
    