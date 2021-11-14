import requests 
from bs4 import BeautifulSoup

req = requests.get("http://www.values.com/inspirational-quotes")

soup = BeautifulSoup(req.content, "html5lib") 

quotes = []

table = soup.find('div', attrs = {'id':'all_quotes'})

print(table.prettify())

for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
  quote = {}
  quote['theme'] = row.h5.text
  quote['url'] = row.a['href']


print(table.prettify())

print('no one:')
print("absolutely no one:")
print('Ivan: "forget about it"\n\n')
print("why are lists in java easier...") 
