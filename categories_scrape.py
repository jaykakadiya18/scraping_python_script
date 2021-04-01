import requests
from bs4 import BeautifulSoup

url = "https://www.etsy.com/uk/help/categories/seller"

r = requests.get(url)
tree = BeautifulSoup(r.content, 'html.parser')

data = []
cata = tree.find_all('li')
f = open('f-data.csv', 'w')
f.write("Categories,Sub-categories-1,Sub-categories-2,Sub-categories-3,Sub-categories-4,Sub-categories-5,Sub-categories-6\n")
for c1 in cata:
    try:
        x= c1.find("span")["data-tooltip"]
        f.write(x.replace(" >",",") + "\n")
        print(x)
    except:
        pass
f.close()