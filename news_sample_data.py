def news_sample():
    return {
        "status": "ok",
        "articles": [
            {
                "source": {"id": "google-news", "name": "Google News"},
                "author": "InfoMoney",
                "title": "Boletim Focus: projeção de inflação é mantida em 5,90% para 2023; estimativa do PIB sobe para 0,85% - InfoMoney",
                "description": "None",
                "url": "https://news.google.com/rss/articles/CBMihAFodHRwczovL3d3dy5pbmZvbW9uZXkuY29tLmJyL2Vjb25vbWlhL2JvbGV0aW0tZm9jdXMtcHJvamVjYW8tZGUtaW5mbGFjYW8tZS1tYW50aWRhLWVtLTU5MC1wYXJhLTIwMjMtZXN0aW1hdGl2YS1kby1waWItc29iZS1wYXJhLTA4NS_SAYgBaHR0cHM6Ly93d3cuaW5mb21vbmV5LmNvbS5ici9lY29ub21pYS9ib2xldGltLWZvY3VzLXByb2plY2FvLWRlLWluZmxhY2FvLWUtbWFudGlkYS1lbS01OTAtcGFyYS0yMDIzLWVzdGltYXRpdmEtZG8tcGliLXNvYmUtcGFyYS0wODUvYW1wLw?oc=5",
                "urlToImage": "None",
                "publishedAt": "2023-03-06T11:36:01Z",
                "content": "None",
            },
            {
                "source": {"id": "google-news", "name": "Google News"},
                "author": "Escola Educação",
                "title": "Novidade: Google Drive agora edita arquivos PDF - Escola Educação",
                "description": "None",
                "url": "https://news.google.com/rss/articles/CBMiTWh0dHBzOi8vZXNjb2xhZWR1Y2FjYW8uY29tLmJyL25vdmlkYWRlLWdvb2dsZS1kcml2ZS1hZ29yYS1lZGl0YS1hcnF1aXZvcy1wZGYv0gEA?oc=5",
                "urlToImage": "None",
                "publishedAt": "2023-03-06T11:30:56Z",
                "content": "None",
            },
        ],
    }


def news_unauthorized_sample():
    return {
        "status": "error",
        "code": "apiKeyMissing",
        "message": "Your API key is missing. Append this to the URL with the apiKey param, or use the x-api-key HTTP header.",
    }
