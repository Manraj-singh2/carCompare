import undetected_chromedriver as uc
#from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os


path =  os.path.join(os.getcwd(), "chromedriver", "chromedriver.exe")



def getUrl(make = None,year= None):


    
    if make and year:
        return f'https://www.cardoor.ca/cars?search=&orderby=0&priceType=cash&price%5Bfrom%5D=10749&price%5Bto%5D=142777&makes%5B{make}%5D%5B%5D=&year%5Bfrom%5D=2013&year%5Bto%5D={year}&miles%5Bfrom%5D=0&miles%5Bto%5D=208000'
    elif make:
        return f'https://www.cardoor.ca/cars?search=&orderby=0&priceType=cash&price%5Bfrom%5D=10749&price%5Bto%5D=142777&makes%5B{make}%5D%5B%5D=&year%5Bfrom%5D=2013&year%5Bto%5D=2025&miles%5Bfrom%5D=0&miles%5Bto%5D=208000'
    elif year:
        return f'https://www.cardoor.ca/cars?search=&orderby=0&priceType=cash&price%5Bfrom%5D=10749&price%5Bto%5D=142777&year%5Bfrom%5D=2013&year%5Bto%5D={year}&miles%5Bfrom%5D=0&miles%5Bto%5D=208000'
    else:
        return 'https://www.cardoor.ca/cars'
    

def openSite(url):

   
    service = Service(executable_path=path)
    driver = uc.Chrome(service=service)

    driver.get(url)

    


