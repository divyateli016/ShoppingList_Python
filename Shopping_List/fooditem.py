from utilities import splitAt
from item import Item
class FoodItem(Item):
    def __init__(self, name, shop, year,needsCooling):
        super().__init__(name, shop, year)
        self.__needsCooling = needsCooling # as a private data member
    @property
    def getNeedsCooling(self):
        return self.__needsCooling
    
    def getNotes(self):
        if self.__needsCooling == False:
            return set()
        else:
            result = set()
            result.add("One or more items require cooling!")
            return result
        
    def toString(self):
        result  = Item.toString(self)
        if self.__needsCooling == True:
            result = result+"[Keep Cool!]"
            return result
        else:
            return result
    
    def save(self,out):
        out.write(f"Food;{self.getName};{self.getShop};{self.getYear};{self.getNeedsCooling}\n")
    
    def __str__(self):#This function is executed when we write print(objectname) as goog as operator << overloading
        return f"Food;{self.getName};{self.getShop};{self.getYear};{self.getNeedsCooling}" #This is the way to access the passed items attributes like name shop and year based on the Food Item class
    
    def restore(line:str):
        indendifier,remain_line = splitAt(line,";")
        if indendifier == "Food":
            name,remainder = splitAt(remain_line,";")
            shop,remainder = splitAt(remainder,";")
            year_str,remainder = splitAt(remainder,";")
            needsCooling = splitAt(remainder,";")
            fooditem = FoodItem(name,shop,int(year_str),bool(needsCooling))
            return fooditem
        else:
            return  None