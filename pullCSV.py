import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
import urllib.request
from io import StringIO

url="https://spotifycharts.com/regional/sv/daily/latest/download"
response=requests.get(url)
# SpicyArray=str(response.content).split(chr(92)+"n")
# reader= csv.reader(SpicyArray,delimiter=',')
# for row in reader:
#     print(row)
#print(f"The length is {len(SpicyArray)}")

reader= csv.reader(str(response.content).split(chr(92)+"n"),delimiter=",")

outPath="Output/test.csv"

with open(outPath, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    for row in reader:

        csvwriter.writerow(row)
        print(row)