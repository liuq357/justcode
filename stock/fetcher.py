import yfinance as yf

# Example: Fetching Apple's stock data
ticker = "AAPL"
data = yf.download(ticker, start="2024-01-01", end="2024-04-01")

print(data)