#Project variables
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Declare variables
smallPizza = 15
mediumPizza = 20
largePizza = 25
pepSmall = 2
pepML = 3
extraCheese = 1
bill = 0

#Calculate Bill
if size == "S":
    bill += smallPizza
elif size == "M":
    bill += mediumPizza
elif size == "L":
    bill += largePizza
else:
    bill += 0

if add_pepperoni == "N":
    bill += 0
elif add_pepperoni == "Y" and size == "S":
    bill += pepSmall
else:
    bill += pepML

if extra_cheese == "N" or extra_cheese == "n":
    bill += 0
else:
    bill += extraCheese

#Display bill
total_bill = f"Your final bill is: ${bill}"
print(total_bill)