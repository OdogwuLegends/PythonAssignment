
inch_of_rain_str = input("Enter the inch of rainfall: ")
inch_of_rain_str = int(inch_of_rain_str)

rainfall_volume = float (inch_of_rain_str * 0.623)

gallons_of_water = rainfall_volume * 231
print("The total gallons of water is: ",gallons_of_water)