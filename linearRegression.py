# linear regression tutorial
import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from matplotlib import style
import pickle

df = Quanl.get('WIKI/GOOGL')

# to check data
print(df.head)

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# define high/low percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

# define percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# define a new dataframe for the data we care about
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

# recheck
print(df.head())

# column to forecast data
forecast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

# math.ceil rounds everything up to the nearest whole number, returns a floats
# trying to predict out 10% of the dataframe from col 'Adj. Close'
forecast_out = int(math.ceil(0.01*len(df)))

# shifting columns negatively or up
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())

# features
x = np.array(df.drop(['labe'], 1))
x_lateley = x[-forecast_out:]
x = x[:-forecast_out]
x = preprocessing.scale(x)

# labels
df.dropna(inplace=True)
y = np.array(df['label'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

# classifier for linear regression algorithm
clf = LinearRegression()

# train on different data than the data that you test
# save the classifier here so you don't have to retrain
clf.fit(x_train, y_train)
with open('linearregression.pickle', 'wb') as f:
    pickle.dump(clf, f)

pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

# with linear regression accuracy is error squared
accuracy = clf.score(x_test, y_test)

forecast_set = clf.predict(x_lately)

print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()

# day in seconds
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.frometimestamp(next_unix)
    next_unix += one_day
    # .loc reference the index of the data frame
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legen(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')

# show plot
plt.show()

# for a different algorithm classifier (svm.SVR)
clf1 = svm.SVR(kernel='poly')
clf1.fit(x_train, y_train)
accuracySVM = clf1.score(x_test, y_test)

print(accuracySVM)
