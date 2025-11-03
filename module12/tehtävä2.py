import requests
API = "0ac37f5cf6173c73889bc8e5c3fe2290"
municipality = input("Enter municipality name: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={API}&units=metric"
try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        temperature=json_response["main"]
        description=json_response["weather"][0]
        print(f"Weather: {description['description']}")
        print(f"Temperature: {temperature['temp']} Celsius")

except requests.exceptions.RequestException as e:
    print("Error")





