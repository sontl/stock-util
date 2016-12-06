print "Enter the price of the stock: "

buy_price = float(raw_input("> "))

no_stock_to_buy = 0

sell_price = buy_price

total_price_buy = 0.0
total_price_sell = 0.0

while (total_price_buy < 4000):
    sell_price += 0.00009
    no_stock_to_buy += 1
    total_price_buy =  buy_price * no_stock_to_buy * 1.025 + 10
    total_price_sell = sell_price * no_stock_to_buy * 0.975 - 10
    
    if (total_price_sell - total_price_buy > 10):
        print '-'*30
        print 'You are buying %d stock with price $%f' % (no_stock_to_buy, buy_price)
        print 'Total price buying is $%f' % total_price_buy
        print 'You have to sell at price $%f to have $10 in profit' % (sell_price)
        print 'Total price selling is $%f' % total_price_sell
        break
    
   