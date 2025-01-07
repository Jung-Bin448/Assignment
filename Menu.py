menu = {
    "pizza" : 750,
    "pasta" : 170,
    "momo" : 130,
    "coffee" : 25
}

print("Welcome to Hamro Cafe")

print("Pizza : 750\nMOMO : 130\nPasta : 170\nCoffee : 25")

total_Amount = 0

item_1 = input("Place your order: ")
if item_1 in menu:
    total_Amount += menu[item_1]
    print(f"{item_1} has been addded to you'r list")
else:
    print(f"{item_1} is not avaiable right now")

another_item = input("Do you want to add more?\nYes/No ")

if another_item == 'yes':
    item_2 = input("Enter the next item you want to order: ")
    if item_2 in menu:
        total_Amount += menu[item_2]
        print(f"{item_2} has been addded to you'r list")
    else:
        print(f"{item_2} is not avaiable right now")


print(total_Amount)