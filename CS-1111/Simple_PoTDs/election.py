__author__ = "Nick Sarris (ngs5st)"

import random

def election_results(trump_chances, clinton_chances, votes):

    trump_elections_won = 0
    clinton_elections_won = 0
    index = 0

    num_runs = int(input('How many simulation runs?: '))
    seed = int(input("Enter a seed (0 for random): "))

    if seed != 0:
        random.seed(seed)

    while index < num_runs:

        state_results = []
        for value in range(0, len(trump_chances)):
            list.append(state_results, random.random())

        idx = 0
        trump_votes = 0
        clinton_votes = 0

        for number in state_results:

            if number < trump_chances[idx]:
                trump_votes = trump_votes + electoral_votes[idx]
            elif number > trump_chances[idx]:
                clinton_votes = clinton_votes + electoral_votes[idx]
            else:
                print ('Something\'s wrong with the RNG')

            idx += 1

        if trump_votes > clinton_votes:
            print ('Run %i: Trump wins with %i' % (index, trump_votes))
            trump_elections_won += 1
        elif trump_votes < clinton_votes:
            print ('Run %i: Clinton wins with %i' % (index, clinton_votes))
            clinton_elections_won += 1
        else:
            print ('The Universe has spoken. Neither candidate is worthy...')
        index += 1

    chance_trump = int(trump_elections_won) / int(num_runs)
    chance_clinton = int(clinton_elections_won) / int(num_runs)
    print ('Chance of Trump Winning:', chance_trump)
    print('Chance of Clinton Winning:', chance_clinton)

trump_states = [.238, .569, .304, .324, .634]
electoral_votes = [13, 29, 20, 9, 18]
clinton_states = []

for value in trump_states:
    list.append(clinton_states, (1 - value))
election_results(trump_states, clinton_states, electoral_votes)