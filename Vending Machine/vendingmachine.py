# step 1

item1 = { "code": 1, "name": "coke", "price": 3, "quantity": 2 }
item2 = { "code": 2, "name": "chips", "price": 2, "quantity": 5 }
item3 = { "code": 3, "name": "chocolate", "price": 4, "quantity": 10 }
item4 = { "code": 4, "name": "water", "price": 1, "quantity": 10 }
item5 = { "code": 5, "name": "juice", "price": 3, "quantity": 5 }
item6 = { "code": 6, "name": "gum", "price": 1, "quantity": 20 }
item7 = { "code": 7, "name": "cookies", "price": 5, "quantity": 8 }
item8 = { "code": 8, "name": "sandwich", "price": 7, "quantity": 3 }

# step 2
while True:
    print("\n")
    print(item1["code"], "\t", item1["name"], "\t", str(item1["price"]))
    print(item2["code"], "\t", item2["name"], "\t", str(item2["price"]))
    print(item3["code"], "\t", item3["name"], "\t", str(item3["price"]))
    print(item4["code"], "\t", item4["name"], "\t", str(item4["price"]))
    print(item5["code"], "\t", item5["name"], "\t", str(item5["price"]))
    print(item6["code"], "\t", item6["name"], "\t", str(item6["price"]))
    print(item7["code"], "\t", item7["name"], "\t", str(item7["price"]))
    print(item8["code"], "\t", item8["name"], "\t", str(item8["price"]))
    print("\n")

    selected = input("Select item by code: ")

    if(selected == "1")and(item1["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item1["price"]or(payment > item1["price"])):
            print("Dispatch coke")
            balance = payment - item1["price"]
            item1["quantity"] = item1["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "2")and(item2["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item2["price"]or(payment > item2["price"])):
            print("Dispatch chips")
            balance = payment - item2["price"]
            item2["quantity"] = item2["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "3")and(item3["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item3["price"]or(payment > item3["price"])):
            print("Dispatch chocolate")
            balance = payment - item3["price"]
            item3["quantity"] = item3["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "4")and(item4["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item4["price"]or(payment > item4["price"])):
            print("Dispatch water")
            balance = payment - item4["price"]
            item4["quantity"] = item4["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "5")and(item5["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item5["price"]or(payment > item5["price"])):
            print("Dispatch juice")
            balance = payment - item5["price"]
            item5["quantity"] = item5["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "6")and(item6["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item6["price"]or(payment > item6["price"])):
            print("Dispatch gum")
            balance = payment - item6["price"]
            item6["quantity"] = item6["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "7")and(item7["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item7["price"]or(payment > item7["price"])):
            print("Dispatch cookies")
            balance = payment - item7["price"]
            item7["quantity"] = item7["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    elif(selected == "8")and(item8["quantity"] > 0):
        payment = int(input("Pay the coins: "))
        if(payment == item8["price"]or(payment > item8["price"])):
            print("Dispatch sandwich")
            balance = payment - item8["price"]
            item8["quantity"] = item8["quantity"] - 1
            print("Balance = " + str(balance))
        else:
            print("Invalid payment, coins returned")

    else:
        print("Invalid code or out of stock")

    control = input("Enter Password to turn off or press any key to select again. ")
    if(control == "12345"):
        break