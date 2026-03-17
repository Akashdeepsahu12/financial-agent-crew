
import matplotlib.pyplot as plt
import os

def generate_chart(hist, ticker):
    os.makedirs("output/charts", exist_ok=True)
    plt.figure()
    hist["Close"].plot(title=f"{ticker} Price Trend")
    path = f"output/charts/{ticker}.png"
    plt.savefig(path)
    plt.close()
    return path
