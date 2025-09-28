from utilities import splitAt
class Item:
    def __init__(self,name,shop,year):
        #For controlled access we use __
        self.__name = name
        self.__shop = shop
        self.__year = year

        #Getter function for the variables which represents the private functions in c++
    @property
    def getName(self):
        return self.__name
    @property
    def getShop(self):
        return self.__shop
    @property
    def getYear(self):
        return self.__year
        
    #function to string return the formated name
    def toString(self):
        stringName = self.__name+"("+self.__shop+")"
        return stringName
    
    def save(self,out):
        out.write(f"Item;{self.__name};{self.__shop};{self.__year}\n")#write function writes the formated strin to the file object passed in the function this is equal to ostream<< means to<< or cout<<

    def __str__(self):
        return f"{self.__name};{self.__shop};{self.__year}"
    
    def getNotes(self):
        return set()
    
    def restore(line:str):
        indendifier,remain_line = splitAt(line,";")
        if indendifier == "Item":
            name,remainder = splitAt(remain_line,";")
            print(name)
            shop,remainder = splitAt(remainder,";")
            print(shop)
            year_str,remainder = splitAt(remainder,";")
            print(year_str)
            item = Item(name,shop,int(year_str))
            return item
        else:
            return  None
        
            


    
        
    