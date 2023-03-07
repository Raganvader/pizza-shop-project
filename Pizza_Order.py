# Required Libraries
import datetime
import csv



# Create superclass 
class Pizza:
    def __init__(self,description,cost):
        self.description =description
        self.cost = cost
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description

# Create subclasses for types of pizza
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Tomato,mozzarella,green basil,mushrooms",100)
    
class MargeritaPizza(Pizza):
    def __init__(self):
        super().__init__("Red tomato sauce,mozzarella,green basil,olive oil",120)
        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Sausage,peppers,mozzarella,oregano,corn",135)

class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Sausage,peppers,olives,mozzarella,onions,corn,garlic powder",160)
    
    

# Create superclass for pizza sauces
class Decorator(Pizza):
    def __init__(self, component,cost,description):

        self.component = component
        self.cost = cost
        self.description = description
    def get_description(self):
        return self.component.get_description() + ' and ' + Pizza.get_description(self)
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
# pizza sauces
class Olives(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,10,"Olives")

class Mushrooms(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,15,"Mushrooms")

class GoatCheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,10,"GoatCheese")

class Meat(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,50,"Meat")

class Onions(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,20,"Onions")

class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,15,"Corn")


def main():
# Printing a menu to the screen
    with open("Menu.txt", "r",encoding = 'utf-8') as f:
        menu = f.read()
        print(menu)
# Get pizza selection from user  
    order = int(input("Can i have your order?: "))
    while order not in [1,2,3,4]:
        order = int(input("Such an option does not exist. Please give an exist Pizza option (1,2,3,4): ")) 
    if order == 1:
        choice = ClassicPizza()
    elif order == 2:
        choice = MargeritaPizza()
    elif order == 3:
        choice = TurkPizza()
    elif order == 4:
        choice = PlainPizza()
    else:
        print("Such an option does not exist.")
# Get pizza sauce selection from user  
    bill = 0
    orderSauce = int(input("What would you like for sauce?: "))
    while orderSauce not in [11,12,13,14,15,16]:
        orderSauce = int(input("Such an option does not exist. Please give an exist Pizza option (11,12,13,14,15,16): ")) 
    if orderSauce == 11:
        description = Olives(choice).get_description()
        bill += Olives(choice).get_cost()
    elif orderSauce == 12:
        description = Mushrooms(choice).get_description()
        bill += Mushrooms(choice).get_cost()
    elif orderSauce == 13:
        description = GoatCheese(choice).get_description()
        bill += GoatCheese(choice).get_cost()
    elif orderSauce == 14:
        description = Meat(choice).get_description()
        bill += Meat(choice).get_cost()
    elif orderSauce == 15:
        description = Onions(choice).get_description()
        bill += Onions(choice).get_cost()
    elif orderSauce == 16:
        description = Corn(choice).get_description()
        bill += Corn(choice).get_cost()
    else:
        print("Such an option does not exist.")
    print("Your Order: ",bill,"TL",description)
   
    time = datetime.datetime.now()
    date = datetime.datetime.strftime(time, '%c')
    
# Get personal information from user

    name = input("Please enter your name: ")
    idNo = input("Please enter your ID number.: ")
    cift_sayilar = ["0","2","4","6","8"]
    while len(idNo) != 11 or idNo[-1] not in cift_sayilar:
        idNo = input("Please enter a valid ID: ")

    cardNo=input("Please enter your credit card number: ")
    while len(cardNo) != 16:
        cardNo = input("Please enter a valid credit card number: ")

    cardPassword = input("Please enter your credit card password: ")
    while len(cardPassword) != 4:
        cardNo = input("Please enter a valid credit card password: ")
    print("\n************  Order Information ***********\n")
    data = [{'Name':name,'ID':idNo,'CardNo':cardNo,'CardPassword':cardPassword,'Order':description,'Date':date}]
    # Writing order information to the screen and transferring the information to the database
    with open("Orders_Database.csv", "a") as file:  
        writer = csv.DictWriter(file, fieldnames=['Name','ID','CardNo','CardPassword','Order','Date'])
        writer.writerows(data)
        file.close()
    with open("Orders_Database.csv", "r") as f:
        menu = f.read()
        print(menu)
        f.close()
main()
