import requests

# Requesting the International Space station API
response = requests.get(
    url="http://api.open-notify.org/iss-now.json",
    timeout=10
)
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (latitude,longitude)

# API request for reverse geo coding

params = {
    "lat": latitude,
    "lon": longitude,
    "format": "json"
}

headers = {
    "User-Agent": "spacestation"
}

# Make the request
response = requests.get(
    url = "https://nominatim.openstreetmap.org/reverse",
    params=params, 
    headers=headers, 
    timeout=10
)
response.raise_for_status()

# Get the data from the response
data = response.json()

# Extract state/state_district and country
address = data.get("address")

print(f"The International Space station current position is: \n Latitude = {latitude}, Longitude = {longitude}")

# If address doesn't exist (over ocean), set defaults
if address is None:
    state = "Ocean"
    country = "Open Water"
else:
    # Try state_district first, if not available use state
    state = address.get("state_district") or address.get("state") or "Unknown"
    country = address.get("country") or "Unknown"

print(f"Location: {state}, {country}")