import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker="AAPL", start="2020-01-01", end="2025-01-01"):
    print(f"🔹 Fetching data for {ticker} from {start} to {end}...")
    data = yf.download(ticker, start=start, end=end)

    if data.empty:
        print("❌ No data fetched. Please check the ticker or date range.")
        return None

    # Save in 'data' folder
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "stock_data.csv")

    data.to_csv(file_path)
    print(f"✅ Data saved successfully at: {file_path}")
    print(f"✅ Total rows fetched: {len(data)}")

    return file_path


if __name__ == "__main__":
    # Example: Fetch Apple stock data
    fetch_stock_data("AAPL", start="2020-01-01", end="2025-01-01")
