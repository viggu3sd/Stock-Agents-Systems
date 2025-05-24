from app.common.alpha_vantage import AlphaVantageClient
from app.agents.ticker_news import ticker_news_agent
from app.agents.ticker_price_change import ticker_price_change_agent

def ticker_analysis_agent(ticker, days=1):
    news = ticker_news_agent(ticker)["news"]
    change = ticker_price_change_agent(ticker, days)
    if "error" in change:
        return {"error": "Insufficient data for analysis"}
    analysis = "The stock price "
    if change["change"] > 0:
        analysis += f"increased by {change['percent']:.2f}% over the last {days} day(s). "
    else:
        analysis += f"decreased by {abs(change['percent']):.2f}% over the last {days} day(s). "
    if news:
        analysis += f"Recent news headlines: {[n['title'] for n in news[:3]]}"
    return {"analysis": analysis}
