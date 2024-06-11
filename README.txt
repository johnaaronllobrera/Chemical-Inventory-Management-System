Chemical Inventory Management System

Author:
- Name: Llobrera, John Aaron B.
- Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
- E-Mail: jbllobrera@up.edu.ph

Code Description:
This Python script provides a menu-driven interface to manage chemical inventory. It allows users to add, view, dispose, restock chemicals, and execute experiments. Chemical details are stored in a dictionary. Users can save and load the inventory from a file.

Features:
- Add new chemical stock to inventory.
- View all chemicals in the inventory.
- Dispose chemicals from inventory.
- Clear all chemicals from inventory.
- Restock chemicals.
- Execute experiments using chemicals from inventory.
- Save and load inventory from a file.

Usage:
1. Run the script.
2. Follow the menu prompts to perform various operations on the chemical inventory.
3. Choose options to add, view, dispose, restock chemicals, save, or load inventory.

Files:
- ims.py: Contains the inventory management system modules.
- inventory.dat: File to store the inventory data.
- ChemicalInventorySystem.py: The main file that will run the modules.

Instructions:
- Make sure Python is installed on your system.
- Run the script main.py using Python.
- Follow the on-screen instructions to manage the chemical inventory.

Example:
MAIN MENU
    [1] Add new Chemical
    [2] View All Chemicals
    [3] Dispose Chemical
    [4] Clear all Chemicals
    [5] Restock Chemical
    [6] Execute Experiment
    [7] Save Inventory
    [8] Load Inventory
    [9] Exit

Enter Choice(1-9): 1

ADD NEW CHEMICAL
    Enter Chemical Code: C001
    Enter Chemical Name: Acetone
    Enter Amount in ml: 500
    Enter Expiry(e.g. 23March2024): 15June2025
    Enter Storage Condition (CHILLED/ROOM): ROOM
Chemical Acetone has been added to inventory.

...

You've exited the program.

Notes:
- The inventory data is stored in a text file named inventory.dat.
- Ensure proper input format while adding chemicals.
- Before exiting, the program saves the inventory automatically.

Feel free to reach out for any questions or suggestions!
