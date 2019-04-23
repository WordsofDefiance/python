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
""")


def add_to_list(input, list):
    list.append(input)
    print('{} was added to the list!'.format(input))
    if len(list) == 1:
        print('There is now one item in this list.')
    else:
        print('There are now {} items in this list.'.format( len(list)) )
    show_list(shopping_list)


def show_list(list):
    clear_screen()
    show_list(shopping_list)
    print("Here's your list:")
    index = 1
    for item in list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)


def clear_screen():
    os.system('cls' if os.name == "nt" else "clear")


# Main loop begins here
show_help()
while True:
    new_item = input("> ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == "SHOW":
        show_list(shopping_list)
        continue

    add_to_list(new_item, shopping_list)

show_list(shopping_list)
