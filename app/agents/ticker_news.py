from app.common.alpha_vantage import AlphaVantageClient

av_client = AlphaVantageClient()

def ticker_news_agent(ticker):
    news = av_client.get_company_news(ticker)
    return {"news": news}
