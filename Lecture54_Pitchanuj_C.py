def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print ("------ iShop ------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculator(totalPrice):
    result = totalPrice*1.07
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1+price2)

if login():
    showMenu()
    x = menuSelect()
    if x == 1:
        print("Total Price (Include VAT):",vatCalculator(int(input("Price (THB): "))))
    elif x ==2:
        print("Total Price (Include VAT):",priceCalculator())
else:
    print("Login Failed")




