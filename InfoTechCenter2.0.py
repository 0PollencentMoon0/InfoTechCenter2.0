# Code Name - Hornet

# Import Libraries Here
from time import sleep  #Print to one line with time delay between prints
import colorama
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

import random

# Welcome Branch
print(Fore.LIGHTMAGENTA_EX + "Welcome to Hornets InfoTechCenter\n"); sleep(1)

print(Fore.LIGHTCYAN_EX + "Hornet's Operating System Booting Up\n"); sleep(1)

# Gas Branch

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    curentGasLevel = random.choice(gasLevelList)
    return curentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = ""
gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements using the Comparative Operator == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1,25), 2)
    if gasLevelIndicator == "Empty":
        print("\n***WARNING YOU ARE ON EMPTY***\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("\n***WARNING***\n Your gas tank is LOW\n The closest gas station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("\nYou are on a QUARTER TANK of gas\nStart planning a visit to a gas station")
    elif gasLevelIndicator == "Half Tank":
        print("\nYou have a HALF Tank of gas\nYou have 125 more miles to empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("\nYou have THREE QUARTER TANK of gas\nYou have 205 more miles to empty")
    else:
        print("\nYou have a FULL Tank of gas, Congratulations.\nYou have 310 more miles to empty")


# Weather Branch

def weather():
    weatherForecast = ["Icy","Snowy","Raining","Windy","Foggy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather Function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forecast of",weatherAlert,":(")
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snowy":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Raining":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    else:
        print("\nWeather is" ,weatherAlert, "let's have a great day!")
        print("VRS will only allow your car to go 120MPH")

# Call Functions Here
vehicleResponseSystem()
gasLevelAlert()