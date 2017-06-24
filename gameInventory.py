# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(inventory):
    print("Inventory:")
    for item in inventory:
        print ("%s:%d" % (item, inventory[item]))
display_inventory(inventory)
   

# Adds to the inventory dictionary a list of items from added_items.
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def add_to_inventory(inventory, added_items):
    update_inventory = dict(Counter(inventory) + Counter(added_items))
    return update_inventory
inventory = add_to_inventory(inventory, added_items)

add_to_inventory(inventory, added_items)
display_inventory(inventory)

   
# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    pass


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
