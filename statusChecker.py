# resources required
import requests
import time 
from bs4 import BeautifulSoup 

# url list to contain number of sites entered by user 
urlsList = []

siteCounter = input("How many sites would you like to monitor?: ")
maxSites = int(siteCounter)

# loop through all sites entered by user and return appropriate responses
while len(urlsList) < maxSites:
    url = input("Paste your url here: ")
    urlsList.append(url)
    for url in urlsList:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(url + " is online")
        except requests.exceptions.RequestException as e:
            print(e)
            SystemExit(1)
