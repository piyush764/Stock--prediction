#%%
import yfinance as yf
#%%
data = yf.download('ADANIPOWER.NS', start='2020-01-01', end='2025-01-01')
print (data.head())

# %%
print(data.shape)
#%%
print(data.head())

# %%
data['Prev_Close'] = data['Close'].shift(1)
#%%
data = data.dropna()
#%%
Y = data['Close']
X = data[['Prev_Close']]
#%%
print(X.head())
print(Y.head())
# %%
