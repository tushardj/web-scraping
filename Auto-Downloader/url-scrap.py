# import os
import bs4
# import requests
# import sys
from urllib.request import urlopen
import autoDownloader


def image_url_scrapper(url):

    connection = urlopen(url)
    raw_html = connection.read()

    connection.close()

    page_soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    container = page_soup.find_all("div", {"class": "item-container"})

    return container


if __name__ == '__main__':
    listout = image_url_scrapper("https://www.newegg.com/p/pl?d=video+cards+for+desktop")
    for elements in listout:
        autoDownloader.download_from_url("http:" + elements.a.img['src'])
        # print(elements.a.img['src'])
