#!/usr/bin/env python3
# Author - Declan Munene
# Date - 24/06/2024
# Description - Script that provides clothing recomendations based # on weather conditions

weather_today = input("What\'s the weather like today? (sunny/rainy/cold): ")

if weather_today == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print("Don\'t forget your umbrella and a raincoat.")
elif weather_today == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don\'t have recommendations for this weather.")
