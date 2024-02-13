# Functions go here

# checks users enter an integer to a given question
def num_check(question):

  while True:

    try:
      response = int(input(question))
      return response

    except ValueError:
      print("Please enter an integer")

# Main routine goes here
tickets_sold = 0

while True:

  name = input("Enter your name or 'xxx' to quit: "")

  if name == "xxx":
    break

  age = int(input("Age: "))

  age = int(input("Enter your age: "))

  if 12 <= age <= 120:
    pass
  elif age < 12:
    print("Sorry, you are too young for this movie")
    continue
  else:
    print("That looks like a mistake - try again")
    continue

  if 12 <= age <= 16:
    cost = 7

  elif 17 <= age <= 65:
    cost = 12
  else:
    cost = 5

  tickets_sold += 1
  print("Ticket price: ${:.2f}".format(cost))


  
    