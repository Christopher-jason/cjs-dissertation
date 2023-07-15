import yfinance as yf

# Set the start and end dates
start_date = '2023-01-01'
end_date = '2023-07-01'

# Get the historical data for S&P 500
sp500 = yf.download('^GSPC', start=start_date, end=end_date)

# Print the stock price data
print(sp500)