import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup

#download chromedriver from https://github.com/mozilla/geckodriver/releases/
DRIVER_PATH = 'drivers/geckodriver'

def get_price(url):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)
    driver.get(url)
    print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    price = soup.find('span', {'itemprop': 'price'})['content']
    driver.quit()
    return price

print(get_price('https://www.scan.co.uk/products/intel-core-i7-10700kf-s-1200-comet-lake-8-cores-16-threads-38ghz-51ghz-turbo-16mb-cache'))

