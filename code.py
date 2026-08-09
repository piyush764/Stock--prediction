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
#%%
X = data[['Prev_Close']]
#%%
print(X.head())
#%%
print(Y.head())

'''<-----SK-LEARN---->'''
#%%
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.2,shuffle=False)

#%%
print(X_test.shape)
#%%
print(X_train.shape)
# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,Y_train)
# %%
predictions = model.predict(X_test)
#%%
print(predictions[:5])
# %%
print(Y_test[:5]) #give actual price on those same day
# %%
