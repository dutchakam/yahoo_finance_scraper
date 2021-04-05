import pandas as pd
import pandas_datareader as web
import datetime as dt

headers = ['Tesla', 'Gamestop', 'Home_Depot', 'Amazon', 'Netflix', 'Google', 'Facebook']

companies = ['TSLA', 'GME', 'HD', 'AMZN', 'NFLX', 'GOOG', 'FB']

# configuring dates so that the program always scrapes data over the course of 1 year
year = dt.datetime.today().year
s = dt.datetime.today().strftime('%Y-%m-%d').replace(str(year), str(year - 1))
e = dt.datetime.today().strftime('%Y-%m-%d')
start = dt.datetime.strptime(s, '%Y-%m-%d').date()
end = dt.datetime.strptime(e, '%Y-%m-%d').date()

df = pd.DataFrame(dict((x, y) for x, y in zip(companies, [[] for a in range(len(companies))])))

for company in companies:
    data = web.DataReader(company, 'yahoo', start, end)
    df[company] = data['Close'].round(2)

df.columns = [(x, y)[1] for x, y in zip(companies, headers)]

df.to_csv('stock_market_close_data.csv')



