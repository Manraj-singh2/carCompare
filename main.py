from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import carDoor


def getData():
    make = input("Enter Brand you want (leave empty to skip): ").strip()
    
    year_input = input("Enter the year you want (YYYY or YY, leave empty to skip): ").strip()

    year = None
    if year_input:  # only process if user entered something
        if len(year_input) == 2:
            year = int("20" + year_input)
        else:
            year = int(year_input)

        if year < 2008 or year > 2025:
            print("No less than 2008 or more than 2025")
            year = None  # reset if invalid

    # brand name
    make = make.lower() if make else None

    return make, year

#defining the main function
def main():
    make, year = getData()
    carDoor.openSite(carDoor.getUrl(make,year))

if __name__ == '__main__':
    main()