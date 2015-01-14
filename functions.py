# Let's learn about functions, the DRY principle,
# function arguments/parameters, and scope.
def display(venue, cost, location):
  #venue
  print(venue, " costs $", str(cost), " and is located at ", location)


print("Chicago Landmarks")
print("-----------------")

display("Wrigley Field", "40", "1033 W. Addison St.")
display("The Bean", 0, "Millenium Park.")
# display()
# display()
# display()

# print("Wrigley Field costs $40 and is located at 1033 W. Addison St.")
# print("The Bean costs $0 and is at Millenium Park.")
# print("The John Hancock Tower costs $35 and is at 875 N. Michigan Ave.")
# print("The United Center costs $75 and is at 1901 W. Madison St.")
# print("The Shakespeare Theater costs $40 is at Navy Pier.")


