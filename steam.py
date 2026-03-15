import requests
from pprint import pprint

base_url = "https://store.steampowered.com/api/storesearch/?term=elden+ring&l=english&cc=US"

def get_name():
    name_list = input("What is the name for the game? ").lower().split(" ")
    final_string = ("+").join(name_list)
    print(final_string)
    return final_string

def get_price_of_game(get_name):
    url = f"https://store.steampowered.com/api/storesearch/?term={get_name}&l=english&cc=US"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data retrieved!")
        game_data = response.json()
        # pprint(game_data)
        number = game_data["items"][0]["id"]
        steam_response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={number}")
        steam_data = steam_response.json()
        if steam_data[str(number)]['data']['is_free'] == True:
            print('The game is free')
        else:
            print(steam_data[str(number)]['data']['price_overview']['final_formatted'])

    else:
        print(f"Failed to retrieve data {response.status_code}")

# game_number = str(1245620)
#
get_price_of_game(get_name())
