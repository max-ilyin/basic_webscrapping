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
    # print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    price = soup.find('span', {'itemprop': 'price'})['content']
    driver.quit()
    return price

def add_prices(p1, p2, p3):
    total = (float(p1) + float(p2) + float(p3))
    return total

cpu = get_price('https://www.scan.co.uk/products/intel-core-i7-10700kf-s-1200-comet-lake-8-cores-16-threads-38ghz-51ghz-turbo-16mb-cache')
motherboard = get_price('https://www.scan.co.uk/products/msi-mag-tomahawk-intel-z490-s-1200-ddr4-sata3-2x-m2-crossfire-25gbe-usb-32-gen1-atx')
ram = get_price('https://www.scan.co.uk/products/16gb-(1x16gb)-corsair-ddr4-vengeance-lpx-black-pc4-19200-(2400)-non-ecc-unbuffered-cas-16-16-16-39-x')

print(add_prices(cpu, motherboard, ram))