"""
Main driver script
"""

from bs4 import BeautifulSoup
import requests
import random
import time
from pprint import pprint
from firms import *
from blockchain import *

TOKEN_PRICE = 100
FUEL_PRICE = 200

DELAY = 1.5

def main():
    bc = BlockChain()
    day = 0
    names = scrapeWebPage()
    firms = []
    for i in range(len(names)):
        firms.append(Firm(names[i], random.randint(10000, 20000), 500, 1000, random.choice([0,1])))

    userFirm = random.choice(firms)
    print("\nWELCOME!\n")
    time.sleep(DELAY)
    print("YOUR FIRM IS:\n")
    time.sleep(DELAY)
    print(userFirm.name + "\n")
    time.sleep(DELAY)
    print("\n\n")

    # MAIN LOOP
    while True:
        print(f"DAY {day}:\n")
        time.sleep(DELAY)
        for i, firm in enumerate(firms):
            print(f"{i}. {firm.name}\n")
        day += 1


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
