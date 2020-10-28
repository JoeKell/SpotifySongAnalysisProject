import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
import urllib.request
from io import StringIO

#The purpose of this code is to pull a list of possible regions for spotify charts.
region_codes=[]
region_names=[]
Original_url="https://spotifycharts.com/regional/global/daily/latest"
list_response=requests.get(Original_url)
soup=BeautifulSoup(list_response.text, "lxml")
#I can add to this later to change from daily or choose another date.
dropdowns=soup.find_all('div', class_='responsive-select')
regions=dropdowns[0].find_all('li')
for region in regions:
    region_codes.append(region['data-value'])
    region_names.append(region.text)



"""url="https://spotifycharts.com/regional/sv/daily/latest/download"
CSVresponse=requests.get(url)
Cleaned_Response=str(CSVresponse.content).split(chr(92)+"n")
Cleaned_Response.pop(202)
Cleaned_Response.pop(0)
reader= csv.reader(Cleaned_Response,delimiter=",")

outPath="Output/test.csv"

with open(outPath, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    for row in reader:
        csvwriter.writerow(["Line"] + row)
        print(row)"""









# #The goal is to get title, description and price from each product on https://scrapingclub.com/exercise/list_basic/
# base_url="https://scrapingclub.com"

# for page in range(1,8):
#     url="https://scrapingclub.com/exercise/list_basic/?page="+str(page)
#     response=requests.get(url)
#     soup=BeautifulSoup(response.text, "lxml")
#     #print(soup)
#     sections=soup.find_all('div', class_='card')
#     for section in sections:
#         if str(section)[:str(section).find(">")+1] != "<div class="+chr(34)+"card"+chr(34)+">":
#             continue
#         Title=section.find('div',class_='card-body').find('a').text
#         Price=section.find('h5').text
#         print(Title,Price)
#         Sub_url=section.find('a')['href']
#         Sub_response=requests.get(base_url+Sub_url)
#         Sub_soup=BeautifulSoup(Sub_response.text, "lxml")
#         Description=Sub_soup.find('p', class_="card-text").text
#         print(Description)