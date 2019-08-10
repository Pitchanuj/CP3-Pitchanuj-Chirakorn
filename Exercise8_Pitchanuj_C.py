usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "member" and passwordInput == "1234":
    print("      Please select the product     ")
    print("(1) Water.....................10 THB")
    print("(2) Coca-Cola.................15 THB")
    print("(3) Potato Chip...............20 THB")
    print("(4) Pocky.....................20 THB")
    userSelection = int(input("Enter product number >>"))
    if userSelection==1:
        waterQ = int(input("[Water] Enter quantity: "))
        print("------------------------------------")
        print("Total Price =", waterQ*10, "THB")
        print("------------------------------------")
        print("Thank you for your purchase :)")
    elif userSelection==2:
        colaQ = int(input("[Coca-Cola] Enter quantity: "))
        print("------------------------------------")
        print("Total Price =",colaQ*15,"THB")
        print("------------------------------------")
        print("Thank you for your purchase :)")
    elif userSelection==3:
        potatoQ = int(input("[Potato Chip] Enter quantity: "))
        print("------------------------------------")
        print("Total Price =",potatoQ*20,"THB")
        print("------------------------------------")
        print("Thank you for your purchase :)")
    elif userSelection==4:
        pockyQ = int(input("[Pocky] Enter quantity: "))
        print("------------------------------------")
        print("Total Price =",pockyQ*20,"THB")
        print("------------------------------------")
        print("Thank you for your purchase :)")
    else:
        print("Product number", userSelection,"does not exist.")
else:
    print("Invalid username or password")
