import requests

base_url = "https://store.steampowered.com/api/appdetails?appids="

def get_price_of_game(number):
    url = f"{base_url}{number}"
    response = requests.get(url)
    print(response)

game_number = 730

get_price_of_game(game_number)