# Author: Llobrera, John Aaron B.
    # Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
    # E-Mail: jbllobrera@up.edu.ph

# Code Description:
    # This Python script provides a menu-driven interface to manage chemical inventory. 
    # It allows users to add, view, dispose, restock chemicals, and execute experiments. 
    # Chemical details are stored in a dictionary. Users can save and load the inventory from a file.

# Import the inventory management system module
from builtins import print
import ims

def load_inventory(inventory):
    # Try to open the inventory file and load its contents into the inventory system
    try:
        with open("inventory.dat", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                stock_code, chem_name, chem_amount, chem_expiry, chem_storage = parts
                # Add each chemical's details to the inventory dictionary
                inventory[stock_code] = [chem_name, int(chem_amount), chem_expiry, chem_storage]
        print("\tInventory loaded successfully.")
    except FileNotFoundError:
        # If the file is not found, start with an empty inventory
        print("Inventory file not found. Starting with empty inventory.")

def save_inventory(inventory):
    # Open the inventory file and save the current state of the inventory system
    with open("inventory.dat", "w") as file:
        for stock_code, details in inventory.items():
            # Write each chemical's details to the file
            line = f"{stock_code},{details[0]},{details[1]},{details[2]},{details[3]}\n"
            file.write(line)
    # Confirm that the inventory has been saved
    print("Inventory saved successfully.")

def display_menu(inventory):
    # Display the main menu and handle user input
    while True:
        print("\n" + "="*15 + " MAIN MENU " + "="*15)
        print("\t[1] Add new Chemical")
        print("\t[2] View All Chemicals")
        print("\t[3] Dispose Chemical")
        print("\t[4] Clear all Chemicals")
        print("\t[5] Restock Chemical")
        print("\t[6] Execute Experiment")
        print("\t[7] Save Inventory")
        print("\t[8] Load Inventory")
        print("\t[9] Exit")
        print("="*46 + "\n")
        choice = input("Enter Choice(1-9): ")
        # Execute the chosen action
        if choice == '1':
            ims.add_stock(inventory)
        elif choice == '2':
            ims.view_stocks(inventory)
        elif choice == '3':
            ims.delete_stock(inventory)
        elif choice == '4':
            ims.delete_all_stocks(inventory)
        elif choice == '5':
            ims.restock_chem(inventory)
        elif choice == '6':
            ims.consume_chem(inventory)
        elif choice == '7':
            save_inventory(inventory)
        elif choice == '8':
            load_inventory(inventory)
        elif choice == '9':
            # Save the inventory before exiting the program
            save_inventory(inventory)
            print("\nYou've exited the program.")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 9.")

def main():
    # Create an empty inventory dictionary
    inventory = {}
    load_inventory(inventory)
    display_menu(inventory)

# Entry point of the program
if __name__ == "__main__":
    main()
