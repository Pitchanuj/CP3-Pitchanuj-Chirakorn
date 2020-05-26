def vatCal(price):
    result = price*(1.07)
    return result
price = int(input("Total Price : "))
print(vatCal(price))