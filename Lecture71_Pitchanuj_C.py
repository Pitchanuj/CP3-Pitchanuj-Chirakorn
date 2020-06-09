menuList=[]
priceList=[]
temp=[[10,10],[20,10]]
print(temp)
print(temp[1])
temp.append([30,20])
print(temp)
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






