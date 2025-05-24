
# Stock Multi-Agent System

A modular multi-agent system for stock analysis using FastAPI and Alpha Vantage.
Developed a multi-agent system using Google ADK (Agent Developer Kit) that can answer 
stock-related questions through modular subagents.

## Features

- Modular agents for:
  - Ticker identification
  - News retrieval
  - Price fetching
  - Price change calculation
  - Price movement analysis
- REST API with FastAPI
- Easy to extend and maintain

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/stock-multi-agent-system.git

cd stock-multi-agent-system



### 2. Install dependencies

pip install -r requirements.txt



### 3. Set up your Alpha Vantage API key

- Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
- Create a `.env` file in the project root:

ALPHA_VANTAGE_KEY=your_actual_api_key_here



### 4. Run the server

uvicorn app.main:app --reload --port 8000



- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API docs.

---

## Sample Queries and Expected Outputs

### Identify Ticker

**Request:**
GET /identify_ticker?query=Tesla


**Response:**
{"ticker": "TSLA"}



### Get News

**Request:**
GET /news?ticker=TSLA


**Response:**
{
"news": [
{ "title": "Tesla hits new milestone...", ... },
...
]
}


### Get Price

**Request:**
GET /price?ticker=TSLA

**Response:**
{"price": 180.45}

### Price Change

**Request:**
GET /price_change?ticker=TSLA&days=7

**Response:**
{
"from": "2024-05-16",
"to": "2024-05-23",
"price_from": 170.00,
"price_to": 180.45,
"change": 10.45,
"percent": 6.15
}

### Analysis

**Request:**
GET /analyze?query=Why did Tesla stock drop today?&days=1

**Response:**
{
"ticker": "TSLA",
"news": {...},
"price": {...},
"price_change": {...},
"analysis": "The stock price decreased by 2.34% over the last 1 day(s). Recent news headlines: ['Tesla faces regulatory scrutiny', 'Market volatility impacts tech stocks']"
}

---

## Architecture

- **FastAPI** for the REST API
- **Alpha Vantage** for stock data and news
- **Modular agent structure** for maintainability

---

## License

MIT (or your chosen license)
