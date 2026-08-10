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
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA10'] = data['Close'].rolling(window=10).mean()
data['Pct_Change'] = data['Close'].pct_change()

#%%
data = data.dropna()
#%%
Y = data['Close']
#%%
X = data[['Prev_Close','MA5','MA10','Pct_Change']]
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
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(Y_test, predictions)
r2 = r2_score(Y_test, predictions)
#%%
print("MSE:", mse) #MSE is √14.19 ≈ ₹3.76 on avg
#%%
print("R2:", r2) #R2 is around94%
