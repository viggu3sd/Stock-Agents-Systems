from app.common.alpha_vantage import AlphaVantageClient

av_client = AlphaVantageClient()

def ticker_price_change_agent(ticker, days=1):
    historical = av_client.get_historical_prices(ticker, days)
    if not historical or len(historical) < days:
        return {"error": "Not enough data"}
    try:
        price_new = float(historical[0][1]["4. close"])
        price_old = float(historical[-1][1]["4. close"])
        change = price_new - price_old
        percent = (change / price_old) * 100
        return {
            "from": historical[-1][0],
            "to": historical[0][0],
            "price_from": price_old,
            "price_to": price_new,
            "change": change,
            "percent": percent
        }
    except Exception as e:
        return {"error": str(e)}
