class Customer:
    name = ""
    lastname = ""
    age = ""
    def addCart(self):
        print("Added to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Pitchanuj"
customer1.lastname = "C"
customer1.addCart()

customer2 = Customer()
customer2.name = "Tony"
customer2.lastname = "Stark"
customer2.addCart()

customer3 = Customer()
customer3.name = "Peter"
customer3.lastname = "Parker"
customer3.addCart()

customer4 = Customer()
customer4.name = "Steve"
customer4.lastname = "Rogers"
customer4.addCart()