menuList=[]
priceList=[]
def showBill():
    totalPrice = 0
    print("My food".center(17,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total Price : ", totalPrice)

while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList)
print(menuList,priceList)
showBill()






