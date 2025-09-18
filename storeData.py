import pandas as pd
import os

def storeData(carName, carKms, carPrice, carYear, carLink):
    df_cars = pd.DataFrame({"Car Name": carName, "Kilometers": carKms, "Price": carPrice, "Year": carYear, "Link": carLink})
    df_cars.to_csv('cars.csv')
    file_exists = os.path.isfile('cars.csv')
    
    df_cars.to_csv(
        'cars.csv', 
        mode='a', 
        index=False, 
        header=not file_exists)

