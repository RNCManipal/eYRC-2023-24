
def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"UPDATED Item {item_name}")
    else:
        inventory[item_name] = quantity
        print(f"ADDED Item {item_name}")


def delete_item(inventory, item_name, quantity):
    if item_name not in inventory:
        print(f"Item {item_name} does not exist")
    else:
        if inventory[item_name] < quantity:
            print(f"Item {item_name} could not be DELETED")
        else:
            inventory[item_name] -= quantity
            print(f"DELETED Item {item_name}")


def calculate_total(inventory):
    return sum(inventory.values())


def manage_inventory():
    t = int(input())  

    for _ in range(t):
        n = int(input()) 
        inventory = {}    

        for _ in range(n):
            item_name, item_quantity = input().split()
            item_quantity = int(item_quantity)
            inventory[item_name] = item_quantity

        m = int(input()) 

        for _ in range(m):
            operation, item_name, quantity = input().split()
            quantity = int(quantity)

            if operation == "ADD":
                add_item(inventory, item_name, quantity)
            elif operation == "DELETE":
                delete_item(inventory, item_name, quantity)

        total_quantity = calculate_total(inventory)
        print(f"Total Items in Inventory: {total_quantity}")

if __name__ == "__main__":
    manage_inventory()
