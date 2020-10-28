import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
import urllib.request
url="https://spotifycharts.com/regional/sv/daily/latest/download"
response=requests.get(url)
SpicyArray=str(response.content).split(chr(92)+"n")
print(f"The length is {len(SpicyArray)}")
for car in SpicyArray:
    car=car.split(",")
    print(car, len(car))