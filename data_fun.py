def get_stock_data(stocks):
    #url for the API to get different stocks+
    listdf=[]
    #stockdata=pd.DataFrame()
    try:
        for stock in stocks:
            url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={:s}&outputsize=full&apikey= 8BH1V7HU7A5NPI12".format(stock)
            response = requests.get(url)
            jsondata=json.loads(response.text)
            df=pd.DataFrame(jsondata['Time Series (Daily)'])
            df=df.transpose()
            df.index.name = 'date'
            df.reset_index(inplace=True)
            df['Company_Symbol']=stock
            df.columns=['date','open','high','low','close','volume','company symbol']
            listdf.append(df)
            stockdata=pd.concat(listdf)
            
    except KeyError:
        print("Key error at",stock)
    return stockdata
    