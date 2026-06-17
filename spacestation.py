import requests

# Requesting the International Space station API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response)
response.raise_for_status()

GPS_data = response.json()
#print(GPS_data)

longitude = GPS_data["iss_position"]["longitude"]
latitude = GPS_data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print("The International Space station current position is ", iss_position)