# Required Libraries
import pandas as pd
import time
import csv

with open("Menu.txt", "r",encoding = 'utf-8') as f:
    menu = f.read()
    print(menu)

# Create superclass
class Pizza:
    def __init__(self,description,cost):
        self.description =description
        self.cost = cost
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description

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
    


class Decorator(Pizza):
    def __init__(self, component,cost,description):
        self.component = component
        self.cost = cost
        self.description = description
    def get_description(self):
        return self.component.get_description() + ' and ' + Pizza.get_description(self)
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    

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




