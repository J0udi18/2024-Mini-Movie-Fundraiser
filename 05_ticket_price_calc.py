# Calculate the tickets price based on the age
def cal_ticket_price(var_age):

# looop for testing...
while True:

  # Get age (assume users input a   valid ineger))
  age = int(input("Age: "))

# calculate ticket cost
ticket_cost = cal_ticket_price(age)
print("Age: {}, Ticket price: ${:.2f}".format(age, ticket_cost)")