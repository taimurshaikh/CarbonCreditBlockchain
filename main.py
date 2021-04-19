"""
Main driver script
"""

from bs4 import BeautifulSoup
import requests
import random

from firms import *

def main():
    names = scrapeWebPage()
    userName = random.choice(names)
    print(names)
    print(userName)

def scrapeWebPage(numFirms = 10):
    """
    Scrapes thomsonreuters to get list of top 100 tech firms to act as placeholder names
    """

    firmNames = []
    page = requests.get("https://www.thomsonreuters.com/en/products-services/technology/top-100.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find_all("tr")
    for tr in res[:10]:
        if tr is not None:
            As = tr.find("a")
            if As is not None:
                firmNames.append(As.text)
    return firmNames

# def generateMarket(firms):
#     res = []
#     for name in firms:
#         res.append(Firm(name, ))

if __name__ == "__main__":
    main()
