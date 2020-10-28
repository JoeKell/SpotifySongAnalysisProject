import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
import urllib.request
from io import StringIO

url="https://spotifycharts.com/regional/sv/daily/latest/download"
response=requests.get(url)
Cleaned_Response=str(response.content).split(chr(92)+"n")
Cleaned_Response.pop(202)
Cleaned_Response.pop(0)
reader= csv.reader(Cleaned_Response,delimiter=",")

outPath="Output/test.csv"

with open(outPath, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    for row in reader:

        csvwriter.writerow(row)
        print(row)