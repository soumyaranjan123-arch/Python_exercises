
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h1')
    for headline in headlines:
        print(headline)

scrape_website('https://docs.google.com/document/u/0/d/1xC2bN4Iiih6hc-0ix2I0uCNJeDqKtLoN/mobilebasic')