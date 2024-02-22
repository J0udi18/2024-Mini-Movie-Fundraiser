#  import statements
import random

import pandas


# functions go here

# checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


# checks user has entered an integer
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can’t be blank, "
                  "please enter your name")


# Checks for an integer more than 0
def int_check(question):
    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)


# Calculate the tickets price based on the age
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

        # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (eg yes / no
#  cash / credit) based on a list of options
def string_checker(question, num_letter, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letter == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)

        print("Please enter a valid response")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# set maximum number of tickets below
MAX_TICKETS = 5
tickets_sold = 0

# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you wan to read the "
                                   "instructions (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    Name = not_blank("Enter your name (or 'xxx' to quit)")

    if Name == 'xxx':
        break

    age = num_check("Age: ")

    # check user is between 12 and 120 (inclusive)
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are to young for this movie")
        continue
    else:
        print("?? That look like a typo, please try again")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("choose a payment method (cash / "
                                "credit): ",
                                2, payment_list)

    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are playing by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(Name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

    # create data frame from dictionary to organise information
    mini_movie_frame = pandas.DataFrame(mini_movie_dict)
    # mini_movie_frame = mini_movie_frame.set_index('Name')

    # Calculate the total ticket cost (ticket + surcharge)
    mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                                + mini_movie_frame['Ticket Price']

    # calculate the profit for rach ticket
    mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

    # calculate ticket and profit totals
    total = mini_movie_frame['Total'].sum()
    profit = mini_movie_frame['Profit'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
    for var_item in add_dollars:
        mini_movie_frame[var_item].apply(currency)

    # choose a winner from our name list
    winner_name = random.choice(all_names)

    # get position of winner name in list
    win_index = all_names.index(winner_name)

    # look up total amount won (ie: ticket price + surcharge)
    total_won = mini_movie_frame.at[win_index, 'Total']

    print("---- Ticket Data ----")
    print()

    # output table with ticket data
    print(mini_movie_frame)

    print()
    print("----- Ticket Cost / Profit -----")

    # output total ticket sales and profit
    print("Total Ticket Sales: ${:.2f}",format(total))
    print("Total Profit : ${:.2f}".format(profit))

    print()
    print('------ Raffle Winner ------')
    print("Congregations {}. You have won ${} ie: your "
          "ticket is free!".format(winner_name, total_won))

    # Output number of tickets sold
    if tickets_sold == MAX_TICKETS:
        print("Congratulations you have sold all the tickets")
    else:
        print("You have sold {} ticket/s. There is {} ticket/s"
              "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
