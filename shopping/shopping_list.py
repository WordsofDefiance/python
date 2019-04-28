import os

# FUNCTIONS/VARIABLES
shopping_list = []

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter "SHOW" to show the current list.
Enter 'HELP for this help.
Enter 'REMOVE to delete an item from your list.
""")
    show_list(shopping_list)


def add_to_list(item, list):
    if len(list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0

    try: 
        position = abs(int(position))
    except ValueError:
        position = None
    if position is 0:
        list.insert(0, item)
    elif position is not None:
        list.insert(position - 1, item)
    else: 
        shopping_list.append(item)
    
    print('{} was added to the list!'.format(item))
    if len(list) == 1:
        print('There is now one item in this list.')
    else:
        print('There are now {} items in this list.'.format( len(list)) )
    show_list(shopping_list)


def show_list(list):
    if len(list) is not 0:
        clear_screen()
    print("Here's your list:")
    index = 1
    for item in list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)


def remove_from_list(list):
    show_list(list)
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        for item in list:
            list.remove(what_to_remove)
    except ValueError:
        pass
    show_list(list)


def clear_screen():
    os.system('cls' if os.name == "nt" else "clear")


# Main loop begins here
show_help()
while True:
    new_item = input("> ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list(shopping_list)
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list(shopping_list)
        continue

    add_to_list(new_item, shopping_list)

show_list(shopping_list)
