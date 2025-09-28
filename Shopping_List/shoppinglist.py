#Note : When calling instance methods in Python → do not pass self explicitly.
##You only see self in the definition, not in the call.
from item import Item
from fooditem import FoodItem
class ShoppingList:
    def __init__(self):
        self.__items:dict[str,list[Item]] = {}#This is like mentioing the sict which takes the string and list of the Items as a types  name: str = "hello"
    
    def __iadd__(self,item:Item):
        shop_name = item.getShop
        if shop_name not in self.__items: #search if the shop name is present
            self.__items[shop_name]=[]#if shopi is not present create or add the shop and [] creates the emty list
        self.__items[shop_name].append(item)# self.__items[shop_name] gives the list of the items available at the shop and then .append adds the new item to the list
        #Just to debug if the items is added successfully
        print(len(self.__items)) # prints the size of the map
        return self #It is as equal to return *this
    
    def printitems(self,year):
        print("Shopping List:\n")
        for shop,items in self.__items.items():# this will give the keys and values separately as single entry in the map
            print(f"{shop}:\n")
            for item in items:
                if item.getYear == year:#Check if the year passed to the function is equal to the year of the specific item
                    print(f"-{item.toString()}\n") # calling the toString function of the each item

    # this function writes the all items to the file
    def save(self,out):
        for shop,items in self.__items.items():
            for item in items:
                item.save(out) #never pass the self while calling the function it should only be given in function definition as a parameter

    def load(self,load_from):
        self.__items.clear()
        for line in load_from:
            line = line.strip()# reomve the \n 
            if not line:
                continue
            item_read = FoodItem.restore(line)
            if item_read is None:
                item_read = Item.restore(line)
            if item_read is not None:
                self+=item_read
                
                
    

    
