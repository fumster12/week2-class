# Let's learn about how to read data from files on disk.

# First, let's talk a bit about strings.




# DEMO: Read the Blackhawks roster from players.txt

file = open("players.txt")
lines = file.readlines()
for name in lines:
  print("****", name, "****")



# CHALLNEGE: Display the number of players on the roster.




# CHALLENGE: Find the average of the numbers in numbers.txt.




# CHALLENGE: Reproduce our fancy list of landmarks using landmarks.txt
# instead of harcoding them.

