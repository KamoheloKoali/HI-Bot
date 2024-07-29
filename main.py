import requests
from bs4 import BeautifulSoup as bs
# import cloudscraper

url = "https://intranet.hbtn.io/projects/2348"

#Load the webpage
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

page = requests.get(url, headers=headers)

#convert to beautiful soup object
soup_obj = bs(page.content, "html.parser")

print(page.status_code)