import requests
from pprint import pprint

def get_name():
    name_list = input("What is the name for the game? ").lower().split(" ")
    final_string = ("+").join(name_list)
    print(final_string)
    return final_string

def get_id(get_name):
    url = f"https://store.steampowered.com/api/storesearch/?term={get_name}&l=english&cc=KZ"
    response = requests.get(url)
    if response.status_code == 200:
        game_data = response.json()
        return game_data["items"][0]["id"]
    else:
        print(f"Failed to retrieve data {response.status_code}")

def get_price_of_game(id):
    steam_response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={id}&cc=KZ")
    steam_data = steam_response.json()
    if steam_data[str(id)]['data']['is_free'] == True:
        print('The game is free')
    else:
        print(steam_data[str(id)]['data']['price_overview']['final_formatted'])


get_price_of_game(get_id(get_name()))
