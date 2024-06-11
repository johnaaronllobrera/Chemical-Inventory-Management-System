def add_stock(inventory):
    print("\nADD NEW CHEMICAL")
    stock_code = input("\tEnter Chemical Code: ")
    
    if stock_code in inventory:
        print("\tChemical with this code already exists.")
        return
    
    chem_name = input("\tEnter Chemical Name: ")
    chem_amount = int(input("\tEnter Amount in ml: "))
    chem_expiry = input("\tEnter Expiry(e.g. 23March2024): ")
    chem_storage = input("\tEnter Storage Condition (CHILLED/ROOM): ")
    
    inventory[stock_code] = [chem_name, chem_amount, chem_expiry, chem_storage]
    print(f"Chemical {chem_name} has been added to inventory.")

def view_stocks(inventory):
    print("\n\tVIEW ALL CHEMICALS")
    for stock_code, details in inventory.items():
        print(f"\n\tChemical Code: {stock_code}, \n\tName: {details[0]},\n\tAmount: {details[1]},\n\tExpiry: {details[2]},\n\tStorage: {details[3]}")

def delete_stock(inventory):
    print("\n\tDISPOSE CHEMICAL")
    stock_code = input("\n\tChemical Code: ")
    if stock_code in inventory:
        del inventory[stock_code]
        print(f"\tChemical with stock code {stock_code} has been disposed.")
    else:
        print("\tChemical does not exist.")

def delete_all_stocks(inventory):
    print("\tCLEAR ALL CHEMICALS")
    inventory.clear()
    print("\n\tAll chemicals have been cleared from inventory.")

def restock_chem(inventory):
    stock_code = input("\t\nEnter stock code to restock: ")
    if stock_code in inventory:
        restock_amount = int(input("\t\nEnter amount to restock: "))
        inventory[stock_code][1] += restock_amount
        print(f"\t\nChemical {inventory[stock_code][0]} restocked by {restock_amount}.")
    else:
        print("\t\nChemical does not exist.")

def consume_chem(inventory):
    stock_code = input("\t\nEnter stock code for experiment: ")
    if stock_code in inventory:
        consume_amount = int(input("\t\nEnter total amount to consume for experiment: "))
        consumed_total = 0
        while consumed_total < consume_amount:
            consume_single = int(input(f"\t\nEnter amount of {inventory[stock_code][0]} to be consumed: "))
            if consume_single <= inventory[stock_code][1]:
                consumed_total += consume_single
                inventory[stock_code][1] -= consume_single
            else:
                print("\t\nNot enough stock for the experiment.")
                continue
        print(f"\t\nChemicals consumed successfully for the experiment.")
    else:
        print("\t\nChemical does not exist.")
