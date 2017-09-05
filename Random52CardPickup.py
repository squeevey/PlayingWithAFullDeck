#File: Random52CardPickup.py
# If you were to randomly find a playing card on the floor every day, 
# how many days would it take to find a full deck?
# Based on the reddit question here
# https://www.reddit.com/r/askscience/comments/6y93j8/if_you_were_to_randomly_find_a_playing_card_on/?utm_content=title&utm_medium=hot&utm_source=reddit&utm_name=frontpage

import random

run_it_x_many_times = 1000
run_counter = 0
list_of_days = []

def HowLongToFillADeck():

	days_to_fill_deck = 0
	deck_list = []

	while len(deck_list) < 52:
		randomcard = random.randint(1,52)
		#print randomcard
		#print deck_list
		if randomcard not in deck_list:
			deck_list.append(randomcard)
		days_to_fill_deck += 1

	return days_to_fill_deck

while run_counter < run_it_x_many_times:

	output = HowLongToFillADeck()
	list_of_days.append(output)
	run_counter += 1


print(list_of_days)
print(sum(list_of_days)/len(list_of_days))
