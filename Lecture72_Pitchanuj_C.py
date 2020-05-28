menuList=[]

def showBill():
    totalPrice = 0
    print("My food".center(17,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("Total Price : ", totalPrice)

while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()