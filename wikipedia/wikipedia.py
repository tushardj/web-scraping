import  bs4
import  requests

req = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

soup = bs4.BeautifulSoup(req.text, 'lxml')

title = soup.select('title')

print("Title of page is: ", title[0].getText())
# this is just to demonstrate how to scrap the page and extract data from it
array = soup.select(".mw-headline")

for element in array:
    print(element.text)
