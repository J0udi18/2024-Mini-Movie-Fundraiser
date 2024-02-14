#  import statements


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
def cal_ticket_price(var_age):

  #ticket is $7.50 for users under 16
  if var_age < 16:
    price = 7.5

  #ticket is $10.50 for users between 16 and 64
  elif var_age < 65:
    price = 10.5

    # ticket proce is $6.50 for seniors (65+)
  else:
    price = 6.5

    return price

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you wan to read the instructions? ")

if want_instructions == "yes":
    print("Instructions go here")

print()


# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    Name = not_blank("Enter your name (or 'xxx' to quit)")

    if name == 'xxx':
        break


    age = num_check("Age: ")

    # check user is between 12 and 120 (inclusive)
    if 12 <= age <= 120:
        print("Sorry you are to young for this movie")
        continue
    else:
        print("?? That look like a typo, please try again")
        continue

    # calculate ticket cost
    tickets_cost = cal_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you haev sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s")