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
    response = requests.get(url, params=params)

    # Parse the response JSON and print the headlines
    if response.status_code == 200:
        articles = response.json()["articles"]
        for article in articles:
            print(article["title"])
        return response.json()
    else:
        print(response.json())
        raise MyNewsException(
            f"Status code {response.status_code}. Failed to retrieve headlines:"
        )


class MyNewsException(Exception):
    pass


print(get_news_by_country("br"))
