from app.common.alpha_vantage import AlphaVantageClient

av_client = AlphaVantageClient()

def identify_ticker_agent(query: str) -> dict:
    """Resolve company name to stock ticker"""
    ticker = av_client.get_ticker(query)
    return {"ticker": ticker} if ticker else {"error": "Ticker not found"}
