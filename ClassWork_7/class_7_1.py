import pyowm 

owm = pyowm.OWM('747e0b601ab68259ae79fec77ba09f68')  # You MUST provide a valid API key



# Search for current weather in London (Great Britain)
userCity = input("Enter your city ")
observation = owm.weather_at_place(userCity)
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

print("Wind", w.get_wind()['speed'], "metres in second")
print("Humidity", w.get_humidity(), "%")
print("Max temperature is ", w.get_temperature('celsius')['temp_max'], "celsium")

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
