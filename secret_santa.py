import random
names = 'amy bob charles david edward fernando gary'.split()
def shuffle_santas(names):
	result, swap, safe = dict(), list(), list()
	# copy the list of names to a new list, then shuffle it
	shuffled_names = names[:]
	random.shuffle(shuffled_names)
	# check for santas who drew themselves
	for santa, giftee in zip(names, shuffled_names):
		if santa == giftee:
			# make a list of santas who need to redraw
			swap.append(santa)
		else:
			safe.append(santa)
			result[santa] = giftee
	for santa in swap:
		# swap giftees with a santa on the safe list
		temp = random.choice(safe)
		result[santa] = result[temp]
		result[temp] = santa
	return result
