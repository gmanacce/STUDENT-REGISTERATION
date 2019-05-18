#### 11 /05 /2019
#####Geofrey Manacce
#### checking multiple condtions with the and condtion

username = input("Welcome, Please enter your username. ")
password = input("Please enter your password. ")
if username != "Geofrey" and password != "password123":
    print("Access denied!")
else:
    print("you are grated!")

your_age = input("How old are you?")
friend_age = input("How old is your friend!")
if int (your_age) >=20 or int (friend_age) >=20:
    print("congrates, one of you is enough to vote!")
else:
    print("you are still under twenty age to vote, wait untill nect year")
    

######How to check names or value in list

#####Name registered

registered_name = ["John","Mary", "Juma","Peter"]

user_name = input("please enter your user name you would like to use ")
if user_name in registered_name:
    print("Sorry! user name already taken")
else:
    print("welcome!, user name is available")
    

#########checking if a value is not in the list

########admin users
Admin_user = ["Geofrey","Ausher"]
########Asking for user name
user_name = input("Please enter you name ")
if user_name not in Admin_user:
    print("Access denied ")
else:
    print("welcom admin")

#############Checking bank interest rate  using if-elif- else statement

###########Get balance
balance = input("please enter you balance")
##use if-elif-else statement
if int(balance) <=100:
    print("you are required to deposite cash")
elif int(balance) <= 100000:
    print("you are granted for big interest rate is 2")
else:
    print("your interest rate will be 4")


######checking multiple condition using if statement.
###create a list a booking details for a certain events.
booking_details = ["Walid", "Ausher", "Geofrey","Getrude"]

if "Walid" in booking_details:
    print('welcome to twenty century cenema!')
if "Aushe" in booking_details:
    print('your sit number is 4 in the middle row')
if "Geofrey" in booking_details:
    print('you will watch in screen two next corner')
if "Getrude" in booking_details:
    print('you will be in the theater around 10pm')
    
#####using FOR and IF statement with list
####creating our shopping cart
shopping_cart = ['pens', 'book', 'paper', 'hand_book']
##adding each item to an order
for item in shopping_cart:
    if item == "pens":
        print("you item is out of order")
    else:
        print("adding" " " + item + " " "to your order")
    
print("thanks for shopping with us, your order is complete!")

######working with empty list using FOR and IF STATEMENT.
#CREATE EMPTY LIST
shopping_cart = ["TOY"]
if shopping_cart:
    for item in shopping_cart:
        print("adding "  + item +" " "to your order" )
    print("your order is complete ")
else:
    print("you must select item before you proceed.")

#####working with two lists

in_stock = ['pens,' 'book','cake','stone']
shopping_cart = ['pens','book','cake','stone','staples']
for item in shopping_cart:
    if item in in_stock:
        print("adding " "" + item + ""  "to you order" )
    else:
        print('sorry you have not added any item into an order')
print('you have a complete order!')
        
