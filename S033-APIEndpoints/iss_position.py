import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
response.raise_for_status()

data = response.json()
print(data)

data_position = response.json()['iss_position']
print(data_position)

longitude = data['iss_position']['longitude']
print(longitude)

latitude = data['iss_position']['latitude']
print(latitude)

iss_position = (longitude, latitude)
print(iss_position)
