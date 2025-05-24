# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables first!
load_dotenv()  

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")
