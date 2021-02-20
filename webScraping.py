import requests
from bs4 import BeautifulSoup
URL = "https://www.worldometers.info/coronavirus/country/india/"
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')
n1 = soup.find('div',attrs = {'class':'container'})
n2 = n1.find_all_next('div',attrs = {'class' : 'row'})
n3 = n2[0].find_all_next('div',attrs = {'class':'col-md-8'})
n4 = n3[0].find_all_next('div',attrs = {'class':'content-inner'})
num5 = n4[0].find_all_next('div',attrs = {'id':'maincounter-wrap'})
cases = num5[0].find_all_next('div',attrs = {'class':'maincounter-number'})
print("Current Cases: " + cases[0].span.text)
deaths = num5[1].find_all_next('div',attrs = {'class':'maincounter-number'})
print("Deaths: "+ deaths[0].span.text)
rec = num5[2].find_all_next('div',attrs = {'class':'maincounter-number'})
print("Recoveries: " + rec[0].span.text)
#print(soup.prettify())
#print(numbers)


