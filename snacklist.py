#list of names + a empty list for the snacks
friends = [ ["Jantje", " "], ["Keesje", " "], ["Pietje", " "] ]


#first loop: asking for the snack and dropping it in de list
for friend in friends:
	friend[1] = input("What is your fave snack, " + friend[0] + "? ")
	print(friend[0] + " likes " + friend[1])
#second loop that prints the names and snacks
for friend in friends:
	print(friend[0] + " likes " + friend[1])
