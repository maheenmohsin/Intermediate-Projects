import requests

API_KEY = "72a46f0e123ec1d875b7219e6a96d9b7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q" : city,
        "appid" : API_KEY,
        "units" : "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data.get("name")
        country = data["sys"].get("country")
        temp = data["main"].get("temp")
        feels_like = data["main"].get("feels_like")
        weather = data["weather"][0].get("description")

        print(f"Location: {city_name}, {country}")
        print(f"Temperature: {temp}C")
        print(f"Feels Like: {feels_like}C")
        print(f"Weather: {weather}\n")
    else:
        print(f"Error {response.status_code}: {response.text}")

def main():
    print("=== Weather App ===")
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Exiting weather app. GoodBye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()