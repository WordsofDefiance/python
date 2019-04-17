TICKET_PRICE = 100
tickets_remaining = 100

# run this code continuously until we run out of tickets
while ( tickets_remaining > 0 ):
    print("There are {} tickets remaining".format(tickets_remaining))

    user = input("What should we call you? ")
    tickets_desired = input("{}, how many tickets would you like to buy? ".format(user));

    def validateInput(input):
        if input.isdigit() is False:
            return False
        elif int(input) > tickets_remaining:
            return False
        else:
            return True

    while ( validateInput(tickets_desired) is not True):
        tickets_desired = input("{}, please use numbers only. You can only buy up to {} tickets. How many tickets would you like to buy? ".format(user, tickets_remaining));

    price = TICKET_PRICE * int(tickets_desired)

    print("Your tickets will cost ${}.".format(price))

    confirm = input( "Do you want to proceed with your purchase? (Y/N) ");


    if confirm.lower() == "y":
        print ("SOLD!")
        tickets_remaining -= int(tickets_desired)
        print('Thanks for your purchase, {}. After your purchase, there are {} tickets remaining'.format(user, tickets_remaining))
    else:
        print("Thanks, anyway, {}.".format(user))

print("There are no tickets available!")
