import os
from pymongo import MongoClient


def database_setup():
    DBUSER = os.getenv("DBUSER")
    DBPASSW = os.getenv("DBPASSW")

    client = MongoClient(
        f"mongodb+srv://{DBUSER}:{DBPASSW}@pokemon.hf2qgqn.mongodb.net/?retryWrites=true&w=majority"
    )

    db = client.pokemonAPI
    cards_db = db.Cards
    cards_db.drop()
    return cards_db
