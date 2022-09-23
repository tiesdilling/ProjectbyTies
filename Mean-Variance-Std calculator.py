import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

df = yf.download(["AAPL","CAT", "TSLA", "KSE"], start = "2000-12-01", end = "2021-12-01")
df = np.log(1+df['Adj Close'].pct_change())

def weightscreator(df) :
    rand = np.random.random(len(df.columns))
    rand /= rand.sum()
    return rand

def portfolioreturn(weights) :
    return np.dot(df.mean(),weights)

df.cov()
def portfoliostd(weights) :
    return (np.dot(np.dot(df.cov(), weights),weights))**(1/2)*np.sqrt(250)

returns = []
stds = []
w = []

print(df.shape)

for i in range(1000) :
    weights = weightscreator(df)
    returns.append(portfolioreturn(weights))
    stds.append(portfoliostd(weights))
    w.append(weights)

plt.scatter(stds, returns)

plt.scatter(min(stds), returns[stds.index(min(stds))], c= "g")
plt.title("Efficient Frontier")
plt.xlabel("PortfolioStd")
plt.ylabel("PortfolioReturn")
plt.show()

print("So, invest in the following way:",w[(stds.index(min(stds)))])
print("And you will recieve these returns:",returns[(stds.index(min(stds)))])
