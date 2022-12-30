<h1 align='center'>Pokemon Price Scraper</h1>

<div align='center'>
    <img src="https://raw.githubusercontent.com/fishsticksnom/pokemon-price-scraper/main/assets/scraper.png" alt="scraper-icon" width="100"/>
</div>

## About
This script gathers the information of different sets of pokemon,including card number, pokemon name, set name,
price raw, price grade nine, and the price graded with ten.

## Dependencies
- bs4
- pymongo
- selenium

## Instructions

```bash
pipenv shell
pipenv install
python3 main.py
```


## Database
How the data is store in the database?

```json
pokemon_card = {
                    "set_name": String,
                    "pokemon_name": String,
                    "card_number": Intenger,
                    "grade_raw":  String,
                    "grade_nine": String,
                    "grade_ten": String,
                }
```

## Notes
**The table is drop every time the script is run.**  
**For getting more sets,the file url can be modify.**  
**To make use of this script Firefox geckodriver is need it.**  


