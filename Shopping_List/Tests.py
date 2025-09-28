#import item
from item import Item
from fooditem import FoodItem
from shoppinglist import ShoppingList


item1 = Item("papaer tissues","Super Market",2027)
print(item1.getName)#in this we are accessing the properties like an attribute hence we need 
print(item1.getShop)
print(item1.getYear)
print(item1.toString())
print(item1)
print(item1.save(open("output.txt","w")))#Creates and open the file and writes 

###############.   Food Item class Tests ##################

foodItem1 = FoodItem("Rice","Super Market",2027,True)
print(foodItem1.getNeedsCooling)
print(foodItem1.toString())
print(foodItem1.getNotes())

print(foodItem1)
foodItem1.save(open("output.txt","a"))#This adds the content at the end of line

####### Shopping list tests#####
list = ShoppingList()
list+=FoodItem("Milk","Super Market",2027,True)
list+=FoodItem("Steak","Super Market",2027,False)
list+=Item("Shampoo","Drug Store",2025)
list.printitems(2027)

item_read = Item.restore("Item;papaer tissues;Super Market;2027")
print(item_read.getName)
print(item_read.getShop)

food_item = FoodItem.restore("Food;Rice;Super Market;2027;True")
print(food_item.getName)
print(food_item.getShop)
print(food_item.getYear)
print(food_item.getNeedsCooling)

######### Loading the file #######
list2 = ShoppingList()
with open("output.txt", "r") as f:
    list2.load(f)
list2.printitems(2027)
