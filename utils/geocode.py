import requests

def geocode_postcode(postcode):
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
    
    