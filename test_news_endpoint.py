import unittest

import responses

import news_sample_data
import newsapi
from news_endpoint import app


class TestNewsAPI(unittest.TestCase):
    @responses.activate
    def test_get_news_success(self):
        # Define the mock response
        mock_response = news_sample_data.news_sample()

        # Register the mock response with responses
        responses.add(responses.GET, newsapi.NEWS_URL, json=mock_response)

        # Make a request to the endpoint
        with app.test_client() as client:
            response = client.get(f"/news/br")
            data = response.get_json()

        # Verify the response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, mock_response["articles"])
        # ...

        # Verify that the API was called with the correct URL
        self.assertEqual(len(responses.calls), 1)
        self.assertIn(newsapi.NEWS_URL, responses.calls[0].request.url)

    @responses.activate
    def test_get_news_401(self):
        # Define the mock response
        mock_response = news_sample_data.news_unauthorized_sample()

        # Register the mock response with responses
        responses.add(responses.GET, newsapi.NEWS_URL, json=mock_response, status=401)

        # Make a request to the endpoint
        with app.test_client() as client:
            response = client.get(f"/news/br")
            data = response.get_json()

        # Verify the response data
        self.assertEqual(response.status_code, 400)

        # Verify that the API was called with the correct URL
        self.assertEqual(len(responses.calls), 1)
        self.assertIn(newsapi.NEWS_URL, responses.calls[0].request.url)
