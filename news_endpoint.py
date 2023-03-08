from flask import Flask, jsonify

import newsapi

app = Flask(__name__)


@app.route("/news/<country>")
def get_news(country):
    result = newsapi.get_news_by_country(country)
    return jsonify(result["articles"])


@app.errorhandler(newsapi.MyNewsException)
def handle_http_error(error):
    return jsonify({"error": str(error)}), 400


@app.errorhandler(Exception)
def handle_request_exception(error):
    return jsonify({"error": "An error occurred while processing the request"}), 500
