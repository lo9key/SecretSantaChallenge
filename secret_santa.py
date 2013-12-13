import random
# placeholder default list of names
names = 'amy bob charles dwight edwardo fernando gary howie'.split()
names = list(range(10000000))
def shuffle_santas(names):
	# copy the list of names to a new list, then shuffle it
	shuffled_names = names[:]
	random.shuffle(shuffled_names)
	# make a dictionary of names, shuffled_names
	result = dict(zip(names,shuffled_names))

	# check the result for santas who drew themselves
	for santa,giftee in result.items():
		while santa == giftee:
			# santa drew themselves, swap with someone else
			temp = random.choice(result.keys())
			result[santa] = result[temp]
			giftee = result[temp] # breaks the while loop
			result[temp] = giftee
	return result

print shuffle_santas(names)
