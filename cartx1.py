from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

my_url = 'https://accounts.cartx.io/orders?type=paid_fulfilled'
LOGIN_URL = 'https://accounts.cartx.io/login'
driver = webdriver.Chrome()
driver.get(LOGIN_URL)

u = driver.find_element_by_name('email')
u.send_keys('XXX@XXX.com')
p = driver.find_element_by_name('password')
p.send_keys('XXXXXXX')
p.send_keys(Keys.RETURN)
#time.sleep(15)
driver.get(my_url)
allrecords = driver.find_element_by_name("orders_list_length")
allrecords.send_keys('Todos')

dados = driver.find_element_by_id("orders_list")
page_html = dados.get_attribute("innerHTML")
page_soup = soup(page_html, 'html.parser')
Links = page_soup.findAll('a', href=True)

with open('some.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Tracking']
#   csv.register_dialect('Dialect.lineterminator')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    n=0
    for n in (range(3, len(page_soup.findAll('td')))[::8]) :
        name = page_soup.findAll('td')[n].text
#        print(name)
        writer.writerow({'Name':name})

    for a in Links:
        order_url = a['href']
        order_page = driver.get(order_url)
        order_page_html = driver.find_element_by_class_name('card-text')
        Tracking = order_page_html.text
        writer.writerow({'Tracking':Tracking})
#        print ("Found the URL:", a['href'])
#        print ("Tracking:", Tracking)





