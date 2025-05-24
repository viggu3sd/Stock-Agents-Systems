from app.common.alpha_vantage import AlphaVantageClient

av_client = AlphaVantageClient()

def ticker_price_agent(ticker):
    price = av_client.get_current_price(ticker)
    return {"price": price} if price else {"error": "Price not found"}
