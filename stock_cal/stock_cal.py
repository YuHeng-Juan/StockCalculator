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

        

print("+--------------------+")
print("|                    |")
print("|    Stock calc      |")
print("|                    |")
print("+--------------------+")

keep = 'y'
while keep=='y':
    mode = int(input("Please choose the mode:\n1. how much you need to pay.\n2. Average price.\n3. SOP FinStock.\n4. average price of Fund\n"))
    if mode==1 :
        cur_price = float(input("Input current price:"))
        num_stock = float(input("Input current number of stock:"))
        mode1_ans = cur_price*num_stock
        print(f"You need to pay {mode1_ans}")
    elif mode == 2:
        avg_price = float(input("Input the average price you bought:"))
        num_stock = float(input("Input the number of stock you bought:"))
        cur_price = float(input("Input the price you buy:"))
        num_buy_stock = float(input("Input the number of stock you buy:"))
        ans = calc_avg_price(avg_price, num_stock, cur_price, num_buy_stock)
        pay = cur_price*num_buy_stock
        print("\nYou need to pay:%.2f" % pay)
        print("Final average price:%.2f" % ans)
    elif mode == 3:
        cur_price = float(input("Input current price:"))
        num_stock = float(input("Input current number of stock:"))
        avg_cash_dividend = float(input("Input average cash dividend:"))
        avg_stock_dividend = float(input("Input average stock dividend:"))

        gradient_price = SOP_down(cur_price,avg_cash_dividend,avg_stock_dividend, 3)
        print("=> After 3 years: {}".format(round(gradient_price,2)))

        high_3_rate = SOP_up(gradient_price,avg_cash_dividend,avg_stock_dividend, 3)
        print("=> High triple rate: {}".format(round(high_3_rate,2)))
        high_6_rate = SOP_up(gradient_price,avg_cash_dividend,avg_stock_dividend, 6)
        print("=> High six rate: {}".format(round(high_6_rate,2)))
    elif mode == 4:
        total_cost = float(input("Input total cost:"))
        num_stock = float(input("Input number of units:"))
        exchange_rate = float(input("Input current exchange rate:"))
        mode4_ans = total_cost/exchange_rate/num_stock
        print("Your average price is:%.2f" % mode4_ans)
    print("Do you wanna keep?[y/n]:",end='')
    keep = input()
    cur_price = ""
    num_buy_stock = ""


print("Bye!")
