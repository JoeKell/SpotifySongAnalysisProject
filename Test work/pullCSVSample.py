import requests
from bs4 import BeautifulSoup
import csv

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

#Open CSV
outPath="Test work/Output/test2.csv"
with open(outPath, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    #Creating a header for the data
    csvwriter.writerow(["Region","Position","Track Name","Artist","Streams","URL"])


#Looping through the region codes and using them in the url to scrape the csv
    for Num,Reg in enumerate(region_codes):
        Current_Region=region_names[Num]
        url=f"https://spotifycharts.com/regional/{Reg}/daily/latest/download"
        CSVresponse=requests.get(url)
        Cleaned_Response=str(CSVresponse.content).split(chr(92)+"n")
        Cleaned_Response.pop(len(Cleaned_Response)-1)
        Cleaned_Response.pop(1)       
        Cleaned_Response.pop(0)
        reader= csv.reader(Cleaned_Response,delimiter=",")
        for row in reader:
            if row[0]=="    <head>":
                break
            csvwriter.writerow([Current_Region] + row)
