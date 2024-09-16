stock_price=[('apple',200),('google',400),('msft',100)]
for item in stock_price:
    print(item)
    for ticker,price in stock_price:
        print(ticker)
        for ticker,price in stock_price:
            print(price+(0.1*price))