from tkinter import *
from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates
from tkinter import ttk
from datetime import timedelta, date

main_window = Tk()
main_window.title("Currency Rates")
main_window.geometry("320x300")
currency_code = CurrencyCodes()
currency_rate = CurrencyRates()
date_obj = date.today()
currency = []
rate30 = []
rate90 = []

for curr in currency_rate.get_rates("USD"):
    currency.append(curr)
currency.sort()

def button_click():
    b = str(base_currency_combobox.get())
    q = str(quote_currency_combobox.get())
    sum30 = 0
    sum90 = 0
    rate = currency_rate.get_rate(b, q, date_obj)
    rate_label.configure(text = "1 " + b + " = " + str(round(rate, 4)) + " " + q)

    previous = date_obj - timedelta(2)
    previous_rate = currency_rate.get_rate(b, q, previous)
    percentage_change = round((rate - previous_rate)/previous_rate * 100, 4)
    if percentage_change > 0:
        change_label1.configure(text="%s appreciates %s%s relative to %s " % (b, str(percentage_change), "%", q))
    elif percentage_change < 0:
        change_label1.configure(text="%s depreciates %s%s relative to %s " % (b, str(abs(percentage_change)), "%", q))
    else:
        change_label1.configure(text="no change")
    change_label2.configure(text = "from %s rates" % (str(previous)))

    for i in range(30):
        dt = date_obj - timedelta(i)
        sum30 += currency_rate.get_rate(b, q, dt)
        rate30.append(currency_rate.get_rate(b, q, dt))
    min30 = round(min(rate30), 4)
    max30 = round(max(rate30), 4)
    avg30 = round((sum30 / 30), 4)

    for j in range(90):
        dt2 = date_obj - timedelta(j)
        sum90 += currency_rate.get_rate(b, q, dt2)
        rate90.append(currency_rate.get_rate(b, q, dt2))
    min90 = round(min(rate90), 4)
    max90 = round(max(rate90), 4)
    avg90 = round((sum90 / 90), 4)

    min30_label.configure(text=min30)
    max30_label.configure(text=max30)
    avg30_label.configure(text=avg30)
    min90_label.configure(text=min90)
    max90_label.configure(text=max90)
    avg90_label.configure(text=avg90)


base_currency_label = Label(main_window, text="From")
base_currency_combobox = ttk.Combobox(main_window, values=currency, width=10)
quote_currency_label = Label(main_window, text = "To")
quote_currency_combobox = ttk.Combobox(main_window, values=currency, width=10)
convert_button = Button(main_window, text="Get Conversion Rate", bg="green", command=button_click)
rate_label = Label(main_window, text ="", font=("Arial", 15))
change_label1 = Label(main_window, text="")
change_label2 = Label(main_window, text="")
blank = Label(main_window, text="")

stats_label = Label(main_window, text="Conversion Rate Statistics", bg='gray', width = 30)
last30_label = Label(main_window, text="Last 30 days")
last90_label = Label(main_window, text="Last 90 days")
min_label = Label(main_window, text="Min")
min30_label = Label(main_window, text="")
min90_label = Label(main_window, text="")
max_label = Label(main_window, text="Max")
max30_label = Label(main_window, text="")
max90_label = Label(main_window, text="")
average_label = Label(main_window, text="Average")
avg30_label = Label(main_window, text="")
avg90_label = Label(main_window, text="")


base_currency_label.grid(row=0, column=1)
quote_currency_label.grid(row=0, column=2)
base_currency_combobox.grid(row=1, column=1)
quote_currency_combobox.grid(row=1, column=2)
convert_button.grid(row=1, column=3)
rate_label.grid(row=4, column=1, columnspan=3)
change_label1.grid(row=5, column=1, columnspan=3)
change_label2.grid(row=6, column=1, columnspan=3)
blank.grid(row=7, column=1)

stats_label.grid(row=8, column=1, columnspan=3)
last30_label.grid(row=9, column=2)
last90_label.grid(row=9, column=3)
min_label.grid(row=10, column=1)
min30_label.grid(row=10, column=2)
min90_label.grid(row=10, column=3)
max_label.grid(row=11, column=1)
max30_label.grid(row=11, column=2)
max90_label.grid(row=11, column=3)
average_label.grid(row=12, column=1)
avg30_label.grid(row=12, column=2)
avg90_label.grid(row=12, column=3)


main_window.mainloop()