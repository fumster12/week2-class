# Let's learn about functions, the DRY principle,
# function arguments/parameters, and scope.
def display(venue, cost, location):
  x = 5
  print(venue, " costs $", str(cost), " and is located at ", location)



print("Chicago Landmarks")
print("-----------------")

display("Wrigley Field", "40", "1033 W. Addison St.")
display("The Bean", 0, "Millenium Park.")
display("The John Hancock Tower", 35, "875 N. Michigan Ave.")
display("The United Center", 75, "1901 W. Madison St.")
display("The Shakespeare Theater", 40, "Navy Pier")

