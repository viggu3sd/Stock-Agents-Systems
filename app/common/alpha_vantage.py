import requests
from app.config import ALPHA_VANTAGE_KEY

class AlphaVantageClient:
    def __init__(self):
        self.base_url = "https://www.alphavantage.co/query"
        self.ticker_map = {
            'tesla': 'TSLA',
            'nvidia': 'NVDA',
            'palantir': 'PLTR',
            'apple': 'AAPL'
        }

    def get_ticker(self, company_name: str) -> str:
        return self.ticker_map.get(company_name.lower(), None)

    def get_company_news(self, ticker: str) -> list:
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": ticker,
            "apikey": ALPHA_VANTAGE_KEY
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return data.get('feed', [])[:5]

    def get_current_price(self, ticker: str) -> float:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": ticker,
            "apikey": ALPHA_VANTAGE_KEY
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return float(data["Global Quote"]["05. price"])

    def get_historical_prices(self, ticker: str, days: int = 7) -> list:
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker,
            "outputsize": "compact",
            "apikey": ALPHA_VANTAGE_KEY
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        daily_data = data.get("Time Series (Daily)", {})
        return list(daily_data.items())[:days]
