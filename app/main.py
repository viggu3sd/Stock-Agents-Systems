from fastapi import FastAPI, Query, HTTPException
from app.config import ALPHA_VANTAGE_KEY
from app.agents.identify_ticker import identify_ticker_agent
from app.agents.ticker_news import ticker_news_agent
from app.agents.ticker_price import ticker_price_agent
from app.agents.ticker_price_change import ticker_price_change_agent
from app.agents.ticker_analysis import ticker_analysis_agent

app = FastAPI()

# Check for API key on startup
if not ALPHA_VANTAGE_KEY:
    raise ValueError("ALPHA_VANTAGE_KEY not found in environment variables")

@app.get("/")
def root():
    return {"message": "Stock Agent System is running!"}

@app.get("/identify_ticker")
async def identify_ticker(query: str = Query(...)):
    try:
        result = identify_ticker_agent(query)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/news")
async def get_news(ticker: str = Query(...)):
    try:
        result = ticker_news_agent(ticker)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/price")
async def get_price(ticker: str = Query(...)):
    try:
        result = ticker_price_agent(ticker)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/price_change")
async def get_price_change(
    ticker: str = Query(...),
    timeframe: str = Query("1d")
):
    try:
        days = 1 if timeframe == "1d" else 7
        result = ticker_price_change_agent(ticker, days)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze")
async def analyze(
    query: str = Query(...),
    timeframe: str = Query("1d")
):
    try:
        ticker_result = identify_ticker_agent(query)
        if "error" in ticker_result:
            raise HTTPException(status_code=404, detail=ticker_result["error"])
        
        ticker = ticker_result["ticker"]
        days = 1 if timeframe == "1d" else 7
        
        return {
            "ticker": ticker,
            "news": ticker_news_agent(ticker),
            "price": ticker_price_agent(ticker),
            "price_change": ticker_price_change_agent(ticker, days),
            "analysis": ticker_analysis_agent(ticker, days)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
