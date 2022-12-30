import time
from bs4 import BeautifulSoup
from selenium import webdriver
from modules.db import database_setup

cards_db = database_setup()


def get_prices(set_name, url):
    driver = webdriver.Firefox()
    driver.get(url)

    time.sleep(3)

    for i in range(1, 6):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    trs = soup.find_all("tr")

    cards = []
    for tr in trs:
        if tr.find("td", {"class": "title"}):
            name_and_number = tr.find("td", {"class": "title"}).a.text.rsplit("#")
            if len(name_and_number) > 1:
                name = name_and_number[0]
                card_number = name_and_number[1]
                grade_raw = tr.find("td", {"class": "used_price"}).span.text
                grade_nine = tr.find("td", {"class": "cib_price"}).span.text
                grade_ten = tr.find("td", {"class": "new_price"}).span.text
                pokemon_card = {
                    "set_name": set_name,
                    "pokemon_name": name,
                    "card_number": int(card_number),
                    "grade_raw": grade_raw,
                    "grade_nine": grade_nine,
                    "grade_ten": grade_ten,
                }
                cards.append(pokemon_card)

    # Populate database here for each loop.
    cards.sort(key=lambda card: card["card_number"])
    cards_db.insert_many(cards)
    driver.close()
    print(f"{set_name} added it into the database.")
    time.sleep(1)
