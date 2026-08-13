import yfinance as yf
import matplotlib.pyplot as plt

TICKER = "AAPL"
PERIOD = "1y"

data = yf.download(TICKER, period=PERIOD)

print(data.head())
print(f"\nRows: {len(data)}")

plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Close"])
plt.title(f"{TICKER} Close Price — {PERIOD}")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(alpha=0.3)
plt.savefig(f"{TICKER}_price.png", dpi=150, bbox_inches="tight")
plt.show()