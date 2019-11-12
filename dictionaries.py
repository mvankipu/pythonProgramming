# # DON'T TOUCH PLEASE!
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# # DON'T TOUCH PLEASE!


# # Use a loop to add together all the donations and store the resulting number in a variable called total_donations
# total_donations = 0

# for v in donations.values():
#     total_donations += v

# total_donations = sum(value for value in donations.values())

# total_donations = sum(donations.values())

# print(total_donations)

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
#found_food = False
#print('Looking for ' + food)
# for k,v in bakery_stock.items():
#     if food == k:
#         print_string = str(v) + ' left'
#         print(print_string)
#         found_food = True
          
#if found_food == False:
#    print('We don\'t make that')

#if food in bakery_stock:
#    print(str(bakery_stock[food]) + ' left')
#else: 
#    print('We don\'t make that')

# quantity_left = bakery_stock.get(food)
# if quantity_left:
#     print(str(quantity_left) + ' left')
# else:
#     print('We don\'t make that')

# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
# #stock_list = {}
# #stock_list.update(inventory)
# stock_list = inventory.copy()
# print(stock_list)

# # add the value 18 to stock_list under the key "cookie"
# #new_dict = {'cookie':18}
# #stock_list.update(new_dict)
# stock_list['cookie'] = 18
# print(stock_list)

# # remove 'cake' from stock_list USE A DICTIONARY METHOD
# stock_list.pop('cake')
# print(stock_list)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# #nswer = {list1[i]:list2[i] for i in range(0,len(list1))}
# answer = dict(zip(list1,list2))
# print(answer)

#person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
#answer = {person[i][0]:person[i][1] for i in range(0,len(person))}
#answer = {k:v for k,v in person}
#answer = dict(person)

#answer = {}.fromkeys('aeiou',0)
#answer = {i:0 for i in 'aeiou'}
#print(answer)

#answer = {i:chr(i) for i in range(65,91)}
answer = {ord(char):char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
print(answer)