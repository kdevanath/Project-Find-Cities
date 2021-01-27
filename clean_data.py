import pandas as pd
import requests

api_key = "oez5tbfb8gztav"

def read_cities():
    filepath = "Resources/cities.csv"
    cities_df = pd.read_csv(filepath, index_col=0)
    us_cities = cities_df.loc[cities_df['Country'] == 'United States']
    print(us_cities)

if __name__ == "__main__":
    read_cities()
    #url = f'https://www.numbeo.com/api/indices?api_key={api_key}&query=Austin, United States'
    url = f'https://www.numbeo.com/api/indices?api_key={api_key}&country=United States'
    print(url)
    response = requests.get(url)
    print(response.json(), response.status_code)
