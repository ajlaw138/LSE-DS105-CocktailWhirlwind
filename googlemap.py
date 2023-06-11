import requests
import pandas as pd

def save_to_csv(data, filename):
    """
    Defining a function save_to_csv to save data to a CSV file. The function takes in two arguments: data, which represents the data to be saved, and filename, which is the name of the CSV file. The function creates a Pandas DataFrame from the data, specifying column names as 'Name' and 'Price Level'. Then, it saves the DataFrame to the specified CSV file and prints a success message.
    :param data:
    :param filename:
    :return:
    """
    df = pd.DataFrame(data, columns=['Name', 'Price Level'])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename} successfully.")

def get_place_details(place_id, api_key):
    """
    Defining a function get_place_details that uses the Google Maps API to fetch details for a given place ID. The function takes in place_id and api_key as arguments. It constructs the API URL with the specified place ID and API key, sends a GET request to the URL, and retrieves the response. The response is then parsed as JSON and returned.
    :param place_id:
    :param api_key:
    :return:
    """
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,price_level&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_place_ids(location, api_key):
    """
    Defining a function get_place_ids that uses the Google Maps API to obtain place IDs for cocktail bars in a specified location. The function takes in location and api_key as arguments. It constructs the API URL with the specified location and API key, sends a GET request to the URL, and retrieves the response. The response is parsed as JSON, and the place IDs are extracted from the 'results' field.
    :param location:
    :param api_key:
    :return:
    """
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=cocktail+bars+in+{location}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    place_ids = [result['place_id'] for result in data['results']]
    return place_ids

def get_price_level(location, api_key):
    place_ids = get_place_ids(location, api_key)
    price_level = []
    for place_id in place_ids:
        details = get_place_details(place_id, api_key)
        if 'price_level' in details['result']:
            name = details['result']['name']
            price = details['result']['price_level']
            price_level.append([name, price])
    return price_level

location = 'London'

API_KEY = "Your API KEY"


level_prices = get_price_level(location, API_KEY)

for name, price_level in level_prices:
    print(f"{name}: {price_level}
    
save_to_csv(level_prices, 'price_level_data.csv')
