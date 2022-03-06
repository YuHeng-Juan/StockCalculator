def calc_avg_price(avg_p, num_stock, cur_price, num_buy_stock):
    ans = ((avg_p*num_stock)+(cur_price*num_buy_stock))/(num_stock+num_buy_stock)
    return ans

def SOP_down(cur_price, avg_cash_dividend, avg_stock_dividend, time):
    if time == 0:
        return cur_price
    else:
        time -= 1
    cost = (cur_price-avg_cash_dividend)/(1+avg_stock_dividend/10)
    return SOP_down(cost,avg_cash_dividend,avg_stock_dividend, time)

def SOP_up(cur_price, avg_cash_dividend, avg_stock_dividend, time):
    for _ in range(time):
        cur_price = cur_price*(1+avg_stock_dividend/10)+avg_cash_dividend
    return cur_price