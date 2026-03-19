from fastapi import FastAPI
from steam import get_name
from steam import get_price_of_game
from steam import get_id
app = FastAPI()

@app.get("/price/{game_name}")
def get_price(game_name):
    price = get_price_of_game(get_id(game_name))
    return {"game": game_name, "price": price}

