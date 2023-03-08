import logging
import os

import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print(NEWS_API_KEY)
NEWS_URL = "https://newsapi.org/v2/top-headlines"


def get_news_by_country(country):
    # Define the base URL and parameters for the News API
    url = NEWS_URL
    params = {
        "country": country,
        "apiKey": NEWS_API_KEY,  # Replace with your API key
    }

    # Send a GET request to the News API
    logging.info(f"Send a GET request to the News API for {country=}, {params=}")
    response = requests.get(url, params=params)

    # Parse the response JSON and print the headlines
    if response.status_code == 200:
        logging.info(f"News API for country {country} succeed {response.json()}")
        return response.json()
    else:
        msg = f"Status code {response.status_code}. Failed to retrieve headlines: {response.json()}"
        logging.error(msg)
        raise MyNewsException(msg)


class MyNewsException(Exception):
    pass


print(get_news_by_country("br"))
