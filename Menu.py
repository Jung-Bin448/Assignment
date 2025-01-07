menu = {
    "Pizza" : 300, #key and value
    "Pasta" : 299,
    "MoMo" : 300,
    "Coffee" : 20
}

print("Welcome to Hamro Cafe")

print("Pizza : 300\nMoMO : 300\nPasta : 299\nCoffee : 20")

total_Amount = 0

item_1 = input("Enter the name of the items you wanna order: ")
if item_1 in menu:
    total_Amount += menu[item_1]
    print(f"The  {item_1} has been addded you you list")
else:
    print("The order you are looking for is not avaiable right now")

another_item = input("Do you wanna order anything else. Yes/No ")

if another_item == 'Yes':
    item_2 = input("Enter the name of the next items you wanna order: ")
    if item_2 in menu:
        total_Amount += menu[item_2]
        print(f"The {item_2} has been addded you you list")
    else:
        print("The order you are looking for is not avaiable right now")


print(total_Amount)