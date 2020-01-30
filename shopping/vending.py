sodas = ["pepsi", "cherry", "sprite"]
chips = ["Doritos", "Fritos"]
candy = ["snikcers", "m&ms", "Twizzlers"]

while sodas or chips or candy:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry!".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
