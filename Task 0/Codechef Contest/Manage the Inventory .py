'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava >
# Filename:         < Manage the Inventory.py >
# Functions:        < add_item,delete_item,calculate_total,manage_inventory,main >
# Global variables: < None >
'''
def add_item(inventory, item_name, quantity):
    '''
    Purpose:
    ---
    Add or update an item in the inventory list.

    Input Arguments:
    ---
    `inventory` :  [dict]
        A dictionary representing the current inventory.

    `item_name` :  [str]
        The name of the item to be added or updated.

    `quantity` :  [int]
        The quantity of the item to be added or updated.

    Returns:
    ---
    None

    Example call:
    ---
    add_item(inventory, "ItemA", 5)
    '''
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"UPDATED Item {item_name}")
    else:
        inventory[item_name] = quantity
        print(f"ADDED Item {item_name}")


def delete_item(inventory, item_name, quantity):
    '''
    Purpose:
    ---
    Delete an item from the inventory list.

    Input Arguments:
    ---
    `inventory` :  [dict]
        A dictionary representing the current inventory.

    `item_name` :  [str]
        The name of the item to be deleted.

    `quantity` :  [int]
        The quantity of the item to be deleted.

    Returns:
    ---
    None

    Example call:
    ---
    delete_item(inventory, "ItemA", 3)
    '''
    if item_name not in inventory:
        print(f"Item {item_name} does not exist")
    else:
        if inventory[item_name] < quantity:
            print(f"Item {item_name} could not be DELETED")
        else:
            inventory[item_name] -= quantity
            print(f"DELETED Item {item_name}")


def calculate_total(inventory):
    '''
    Purpose:
    ---
    Calculate the total quantity of items in the inventory list.

    Input Arguments:
    ---
    `inventory` :  [dict]
        A dictionary representing the current inventory.

    Returns:
    ---
    `total_quantity` :  [int]
        The total quantity of items in the inventory.

    Example call:
    ---
    total = calculate_total(inventory)
    '''
    return sum(inventory.values())


def manage_inventory():
    '''
    Purpose:
    ---
    Main function to manage the lab inventory.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    manage_inventory()
    '''
    test_cases = int(input())  # Number of test cases

    for _ in range(test_cases):
        n = int(input())  
        #n: Number of items in the lab initially
        inventory = {}    # Initialize the inventory dictionary

        # Populate the initial inventory
        for _ in range(n):
            item_name, item_quantity = input().split()
            item_quantity = int(item_quantity)
            inventory[item_name] = item_quantity

        m = int(input()) 
        # m: Number of operations to perform

        # Process the operations
        for _ in range(m):
            operation, item_name, quantity = input().split()
            quantity = int(quantity)

            if operation == "ADD":
                add_item(inventory, item_name, quantity)
            elif operation == "DELETE":
                delete_item(inventory, item_name, quantity)

        # Calculate and print the total quantity of items in the inventory
        total_quantity = calculate_total(inventory)
        print(f"Total Items in Inventory: {total_quantity}")

# Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    To call the manage_inventory() function to perform further operations.
if __name__ == "__main__":
    manage_inventory()
