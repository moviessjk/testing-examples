import unittest
from unittest.mock import patch

import responses

import newsapi
from news_sample_data import news_sample, news_unauthorized_sample


class TestNewsAPI(unittest.TestCase):
    @responses.activate
    @patch("newsapi.logging")
    def test_get_news_success(self, mock_logging):
        # Define the mock response data
        mock_data = news_sample()
        # Add the mock response to responses
        responses.add(responses.GET, newsapi.NEWS_URL, json=mock_data, status=200)

        # Call the News API endpoint
        result = newsapi.get_news_by_country("br")

        # Verify that the mock response is returned
        self.assertEqual(result, mock_data)

        # Verify that only one request was made to the News API
        self.assertEqual(len(responses.calls), 1)
        self.assertIn(newsapi.NEWS_URL, responses.calls[0].request.url)
        self.assertEqual(mock_logging.info.call_count, 2)
        mock_logging.error.assert_not_called()

    @responses.activate
    @patch("newsapi.logging")
    def test_get_news_401(self, mock_logging):
        # Define the mock response data
        mock_data = news_unauthorized_sample()

        # Add the mock response to responses
        responses.add(responses.GET, newsapi.NEWS_URL, json=mock_data, status=401)

        # Call the News API endpoint
        with self.assertRaises(newsapi.MyNewsException) as e:
            newsapi.get_news_by_country("br")

        # Verify that only one request was made to the News API
        self.assertEqual(len(responses.calls), 1)
        self.assertIn("Status code 401", e.exception.args[0])
        self.assertIn(newsapi.NEWS_URL, responses.calls[0].request.url)
        mock_logging.error.assert_called_once()
