# Let's learn about lists and iteration so we can automate things.

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)


# 1. CODE-ALONG: Use a while loop (or a repeat loop) to simplify our code.
# number = 1
# while (number <= 5):
#   print(number)
#   print("Go Hawks")
#   number = number + 1


# 2. CODE-ALONG: Use a for loop (combined with a range) to generalize our code.
#    (also use IDLE to experiment)

# for number in range(6,12):
#   print(number)


# 3. CODE-ALONG: Use a for loop (combined with a list) to generalize our code.

# my_list = [1,"Apple","Banana",4,5]
# for item in my_list:
#   print(item)


# 4. CHALLENGE: Choose a list structure and a looping construct to automate this code as much as you can:

# print("Wrigley Field")
# print("The Bean")
# print("The John Hancock Tower")
# print("The United Center")
# print("The Shakespeare Theater")

# SOLUTION (this is just one of many possible):
#
# landmarks = ["Wrigley Field", "The Bean", "The John Hancock Tower",
#               "The United Center", "The Shakespeare Theater"]
# for place in landmarks:
#   print(place)


# 5. CHALLENGE: Write a function that accepts a list of landmark names you want to visit
# and displays the total cost of the trip.  Use the cost information from functions.py.

def calculate_total_cost(places):
  cost = 0
  for place in places:
    if place == "Wrigley Field":
      cost = cost + 40
    elif place == "The John Hancock Tower":
      cost = cost + 35
    elif place == "The United Center":
      cost = cost + 75
    elif place == "The Shakespeare Theater":
      cost = cost + 40
  print("Your trip will cost $" + str(cost))

# Let's go to a couple of places.
calculate_total_cost(["The United Center", "The Shakespeare Theater"])


# 6. CHALLENGE: Go back to warmup.py, and enhance the code so that
# the user can keep guessing until they get it right.
#
# SOLUTION: See extra.py for the solution.

