import pandas as pd

def read_cities():

    df = pd.read_csv('cities.csv')
    cities = df.to_dict(orient='records')
    return cities