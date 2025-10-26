import undetected_chromedriver as uc
#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import os

from abc import ABC
from carScraper import CarScraper


path =  os.path.join(os.getcwd(), "chromedriver", "chromedriver.exe")


class Clutch(CarScraper,ABC):
    def getUrl(self,make = None,year=  None):

        if make and year:
            self.url = f'https://www.clutch.ca/cars/{make}?yearLow=2015&yearHigh={year}'
        elif make:
            self.url = f'https://www.clutch.ca/cars/{make}'
        elif year:
            self.url = f'https://www.clutch.ca/cars?yearLow=2015&yearHigh={year}'
        else:
            self.url = 'https://www.clutch.ca/cars'

        return self.url
        


    def getCars(self):

   
        service = Service(executable_path=path)
        driver = uc.Chrome(service=service)

        driver.get(self.url)

        

        products = driver.find_elements(By.XPATH,'//div[contains(@class,"MuiStack-root")]')
        

        for product in products:
            try:  
                # Used dot to make it relative to the current product

                #get the title
                title = product.find_element(By.XPATH, './/h3[contains(@class,"MuiTypography-root")]')
                
                
                #getLink of the car
                link = product.find_element(By.XPATH, './/div[contains(@class, "product-title")]/a').get_attribute("href")
                


                #get Kilometers
                Kms = product.find_element(By.XPATH,'.//div[contains(@class, "product-description")]')
                

                #get price
                price = product.find_element(By.XPATH,'.//span[contains(@class,"actual-price")]')
                

                if title.text not in self.carName:
                    title = title.text.split(' ')
                    year = title[0]
                    self.carName.append(" ".join(title[1:]))
                    self.carYear.append(year)
                    self.carLink.append(link)
                    self.carKms.append(Kms.text.split("|")[1])
                    self.carPrice.append(price.text)
            except:
                pass
            finally:
                driver.quit()
