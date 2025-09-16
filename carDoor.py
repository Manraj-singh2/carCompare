import undetected_chromedriver as uc
#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import os

from abc import ABC
from carScraper import CarScraper


path =  os.path.join(os.getcwd(), "chromedriver", "chromedriver.exe")


class carDoor(CarScraper,ABC):
    def getUrl(self,make = None,year=  None):

        if make and year:
            self.url = f'https://www.cardoor.ca/cars?search=&orderby=0&priceType=cash&price%5Bfrom%5D=10749&price%5Bto%5D=142777&makes%5B{make}%5D%5B%5D=&year%5Bfrom%5D=2013&year%5Bto%5D={year}&miles%5Bfrom%5D=0&miles%5Bto%5D=208000'
        elif make:
            self.url = f'https://www.cardoor.ca/cars?search=&orderby=0&priceType=cash&price%5Bfrom%5D=10749&price%5Bto%5D=142777&makes%5B{make}%5D%5B%5D=&year%5Bfrom%5D=2013&year%5Bto%5D=2025&miles%5Bfrom%5D=0&miles%5Bto%5D=208000'
        elif year:
            self.url = f'https://www.cardoor.ca/cars?search=&orderby=0&priceType=cash&price%5Bfrom%5D=10749&price%5Bto%5D=142777&year%5Bfrom%5D=2013&year%5Bto%5D={year}&miles%5Bfrom%5D=0&miles%5Bto%5D=208000'
        else:
            self.url = 'https://www.cardoor.ca/cars'

        return self.url
        

    def getCars(self):

   
        service = Service(executable_path=path)
        driver = uc.Chrome(service=service)

        driver.get(self.url)

        products = driver.find_elements(by='xpath',value='//div[contains(@class,"item-box")]')

        for product in products:
            try:
                # Used dot to make it relative to the current product

                #get the title
                title = product.find_element(By.XPATH, './/div[contains(@class, "product-title")]')
                self.carName.append(title.text.split(" ")[1])
                self.carYear.append(title.text.split(" ")[0])

                #getLink of the car
                link = product.find_element(By.XPATH, './/div[contains(@class, "product-title")]/a').get_attribute("href")
                self.carLink.append(link)


                #get Kilometers
                Kms = product.find_element(By.XPATH,'.//div[contains(@class, "product-description")]')
                self.carKms.append(Kms.text.split("|")[1])

                #get price
                price = product.find_element(By.XPATH,'.//span[contains(@class,"actual-price")]')
                self.carPrice.append(price.text)

            except:
                # Alternative approach if the first one fails
                self.carName.append("Data not available")


        driver.quit()


    



    



    


