import tkinter as tk
import StockFunction

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Stock Calculator')
        self.geometry('1000x500')
        # self.init_mode()
        self.fr1 = tk.Frame(self,  width=1000 , height=50)
        self.fr2 = tk.Frame(self,  width=250)
        self.fr3 = tk.Frame(self,  width=250)
        self.fr4 = tk.Frame(self,  width=500)

        self.fr1.grid(column=0, row=0, columnspan=3)
        self.fr2.grid(column=0, row=1)
        self.fr3.grid(column=1, row=1)
        self.fr4.grid(column=2, row=1)
        self.align_mode = 'nswe'
        # frame 1 title
        label_title = tk.Label(self.fr1, text="Stock Calculator", font=('Arial', 20))
        label_title.grid(column=0, row=0)
        
        self.init_mode()

    # 清空 Frame 中的控制物件
    def clear_frame(self, frame): 
        for widget in frame.winfo_children():
            widget.destroy()

    def init_mode(self):
        label_mode = tk.Label(self.fr2, text="Mode", bg='light gray', font=('Arial', 12))
        label_mode.grid(column=0, row=0, sticky=self.align_mode)

        button_mode1 = tk.Button(self.fr2, text="1. how much you need to pay", anchor=tk.NW, command=self.btn1_event)
        button_mode2 = tk.Button(self.fr2, text="2. Average price", anchor=tk.NW, command=self.btn2_event)
        button_mode3 = tk.Button(self.fr2, text="3. SOP FinStock", anchor=tk.NW, command=self.btn3_event)
        button_mode4 = tk.Button(self.fr2, text="4. Average price of Fund", anchor=tk.NW ,command=self.btn4_event)
        button_mode1.grid(column=0, row=1,sticky=self.align_mode)
        button_mode2.grid(column=0, row=2,sticky=self.align_mode)
        button_mode3.grid(column=0, row=3,sticky=self.align_mode)
        button_mode4.grid(column=0, row=4,sticky=self.align_mode)

    def btn1_event(self):
        self.clear_frame(self.fr3)
        self.clear_frame(self.fr4)

        cur_price = tk.DoubleVar()
        num_stock = tk.DoubleVar()
        input1_label = tk.Label(self.fr3, text='Input current price:',anchor=tk.NE)
        input1_entry = tk.Entry(self.fr3, textvariable=cur_price)
        input1_label.grid(column=0, row=0, sticky=self.align_mode)
        input1_entry.grid(column=1, row=0, sticky=self.align_mode)

        input2_label = tk.Label(self.fr3, text='Input current number of stock:',anchor=tk.NE)
        input2_entry = tk.Entry(self.fr3, textvariable=num_stock)
        input2_label.grid(column=0, row=1, sticky=self.align_mode)
        input2_entry.grid(column=1, row=1, sticky=self.align_mode)

        result = tk.Button(self.fr3, text="Get Result", command=lambda: self.result(1, cur_price=cur_price.get(), num_stock=num_stock.get()))
        result.grid(column=1, row=2, sticky=self.align_mode)

    def btn2_event(self):
        self.clear_frame(self.fr3)
        self.clear_frame(self.fr4)

        avg_price = tk.DoubleVar()
        num_stock = tk.DoubleVar()
        cur_price = tk.DoubleVar()
        num_buy_stock = tk.DoubleVar()

        input1_label = tk.Label(self.fr3, text='Input the average price you bought:',anchor=tk.NE)
        input1_entry = tk.Entry(self.fr3, textvariable=avg_price)
        input1_label.grid(column=0, row=0, sticky=self.align_mode)
        input1_entry.grid(column=1, row=0, sticky=self.align_mode)

        input2_label = tk.Label(self.fr3, text='Input the number of stock you bought:',anchor=tk.NE)
        input2_entry = tk.Entry(self.fr3, textvariable=num_stock)
        input2_label.grid(column=0, row=1, sticky=self.align_mode)
        input2_entry.grid(column=1, row=1, sticky=self.align_mode)

        input3_label = tk.Label(self.fr3, text='Input the price you buy:',anchor=tk.NE)
        input3_entry = tk.Entry(self.fr3, textvariable=cur_price)
        input3_label.grid(column=0, row=2, sticky=self.align_mode)
        input3_entry.grid(column=1, row=2, sticky=self.align_mode)

        input4_label = tk.Label(self.fr3, text='Input the number of stock you buy:',anchor=tk.NE)
        input4_entry = tk.Entry(self.fr3, textvariable=num_buy_stock)
        input4_label.grid(column=0, row=3, sticky=self.align_mode)
        input4_entry.grid(column=1, row=3, sticky=self.align_mode)

        result = tk.Button(self.fr3, text="Get Result", command=lambda: self.result(2, avg_price=avg_price.get(), num_stock=num_stock.get(), cur_price=cur_price.get(), num_buy_stock=num_buy_stock.get()))
        result.grid(column=1, row=4, sticky=self.align_mode)

    def btn3_event(self):
        self.clear_frame(self.fr3)
        self.clear_frame(self.fr4)

        cur_price = tk.DoubleVar()
        num_stock = tk.DoubleVar()
        avg_cash_dividend = tk.DoubleVar()
        avg_stock_dividend = tk.DoubleVar()

        input1_label = tk.Label(self.fr3, text='Input current price:',anchor=tk.NE)
        input1_entry = tk.Entry(self.fr3, textvariable=cur_price)
        input1_label.grid(column=0, row=0, sticky=self.align_mode)
        input1_entry.grid(column=1, row=0, sticky=self.align_mode)

        input2_label = tk.Label(self.fr3, text='Input current number of stock:',anchor=tk.NE)
        input2_entry = tk.Entry(self.fr3, textvariable=num_stock)
        input2_label.grid(column=0, row=1, sticky=self.align_mode)
        input2_entry.grid(column=1, row=1, sticky=self.align_mode)

        input3_label = tk.Label(self.fr3, text='Input average cash dividend:',anchor=tk.NE)
        input3_entry = tk.Entry(self.fr3, textvariable=avg_cash_dividend)
        input3_label.grid(column=0, row=2, sticky=self.align_mode)
        input3_entry.grid(column=1, row=2, sticky=self.align_mode)

        input4_label = tk.Label(self.fr3, text='Input average stock dividend:',anchor=tk.NE)
        input4_entry = tk.Entry(self.fr3, textvariable=avg_stock_dividend)
        input4_label.grid(column=0, row=3, sticky=self.align_mode)
        input4_entry.grid(column=1, row=3, sticky=self.align_mode)

        result = tk.Button(self.fr3, text="Get Result", command=lambda: self.result(3, cur_price=cur_price.get(), num_stock=num_stock.get(), avg_cash_dividend=avg_cash_dividend.get(), avg_stock_dividend=avg_stock_dividend.get()))
        result.grid(column=1, row=4, sticky=self.align_mode)

    def btn4_event(self):
        self.clear_frame(self.fr3)
        self.clear_frame(self.fr4)

        total_cost = tk.DoubleVar()
        num_stock = tk.DoubleVar()
        exchange_rate = tk.DoubleVar()

        input1_label = tk.Label(self.fr3, text='Input total cost:',anchor=tk.NE)
        input1_entry = tk.Entry(self.fr3, textvariable=total_cost)
        input1_label.grid(column=0, row=0, sticky=self.align_mode)
        input1_entry.grid(column=1, row=0, sticky=self.align_mode)

        input2_label = tk.Label(self.fr3, text='Input number of units:',anchor=tk.NE)
        input2_entry = tk.Entry(self.fr3, textvariable=num_stock)
        input2_label.grid(column=0, row=1, sticky=self.align_mode)
        input2_entry.grid(column=1, row=1, sticky=self.align_mode)

        input3_label = tk.Label(self.fr3, text='Input current exchange rate:',anchor=tk.NE)
        input3_entry = tk.Entry(self.fr3, textvariable=exchange_rate)
        input3_label.grid(column=0, row=2, sticky=self.align_mode)
        input3_entry.grid(column=1, row=2, sticky=self.align_mode)

        result = tk.Button(self.fr3, text="Get Result", command=lambda: self.result(4, total_cost=total_cost.get(), num_stock=num_stock.get(), exchange_rate=exchange_rate.get()))
        result.grid(column=1, row=4, sticky=self.align_mode)

    def result(self, mode, **data):
        self.clear_frame(self.fr4)

        if mode == 1:
            mode1_ans = data['cur_price'] * data['num_stock']
            output_label = tk.Label(self.fr4, text="You need to pay: {}".format(mode1_ans))
            output_label.grid(column=0, row=0, sticky=self.align_mode)

        elif mode == 2:
            mode2_ans = StockFunction.calc_avg_price(data['avg_price'], data['num_stock'], data['cur_price'], data['num_buy_stock'])
            mode2_pay = data['cur_price'] * data['num_buy_stock']
            output_label = tk.Label(self.fr4, text="You need to pay: {}".format(mode2_pay), anchor=tk.NE)
            output_label.grid(column=0, row=0, sticky=self.align_mode)
            output_labe2 = tk.Label(self.fr4, text="Final average price: {}".format(mode2_ans), anchor=tk.NE)
            output_labe2.grid(column=0, row=1, sticky=self.align_mode)

        elif mode == 3:
            mode3_gradient_price = StockFunction.SOP_down(data['cur_price'], data['avg_cash_dividend'], data['avg_stock_dividend'], 3)
            mode3_high_3_rate = StockFunction.SOP_up(mode3_gradient_price, data['avg_cash_dividend'], data['avg_stock_dividend'], 3)
            mode3_high_6_rate = StockFunction.SOP_up(mode3_gradient_price, data['avg_cash_dividend'], data['avg_stock_dividend'], 6)

            output_label = tk.Label(self.fr4, text="After 3 years: {}".format(round(mode3_gradient_price, 2)), anchor=tk.NE)
            output_label.grid(column=0, row=0, sticky=self.align_mode)
            output_labe2 = tk.Label(self.fr4, text="High triple rate: {}".format(round(mode3_high_3_rate, 2)), anchor=tk.NE)
            output_labe2.grid(column=0, row=1, sticky=self.align_mode)
            output_labe3 = tk.Label(self.fr4, text="High sextuple rate: {}".format(round(mode3_high_6_rate, 2)), anchor=tk.NE)
            output_labe3.grid(column=0, row=2, sticky=self.align_mode)

        elif mode == 4:
            mode4_ans = data['total_cost']/data['exchange_rate']/data['num_stock']
            output_label = tk.Label(self.fr4, text="Your average price is: {}".format(round(mode4_ans, 2)), anchor=tk.NE)
            output_label.grid(column=0, row=0, sticky=self.align_mode)

        
    
    
if __name__ == "__main__":
    app = Window()
    app.mainloop()
