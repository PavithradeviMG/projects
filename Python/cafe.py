# create amenu using list
menu = ["Black coffee","Latte","Cappuccino","Espresso"]
# Initiate the item_value to calculate it
item_value = 0
#Create a stock & price list  for the menu using dictionary
stock = {"Black coffee" : 6,
       "Latte" : 7,
       "Cappuccino" : 9,
         "Espresso" : 10 }
price = {"Black coffee" : 7,
       "Latte" : 8,
       "Cappuccino" : 10,
         "Espresso" : 12 }
# Using a for loop to calculate the item_value
for item in menu:
    item_value += stock[item] * price[item] 
    print(item_value)
  