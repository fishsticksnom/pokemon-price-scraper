from modules.data import urls
from modules.scraper import get_prices


def main():
    for set_name, url in urls.items():
        get_prices(set_name, url)


if __name__ == "__main__":
    main()
