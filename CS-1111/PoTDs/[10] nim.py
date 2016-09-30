__author__ = "Nick Sarris"

def computer_turn(marbles):

    if marbles != 0:
        print ("The pile has %s marbles in it" % marbles)
        computer_list = list(range(int(marbles / 2) + 1))
        computer_list.remove(0)
        new_marbles = int(marbles)

        prime_list = list(range(1, 1001))
        two_primes = []

        for i in prime_list:
            list.append(two_primes, (2 ** i) - 1)

        for i in computer_list:
            i = marbles - i
            if i in two_primes:
                new_marbles = i
                print ("The computer takes %s marbles" % (marbles - i))
                if new_marbles == 0:
                    print ("Congratulations! You win!")
                    print ('')
                return new_marbles

        if new_marbles == marbles:
            print("The computer takes %s marbles" % (1))
            new_marbles = marbles - 1
            if new_marbles == 0:
                print ("Congratulations! You win!")
                print ('')
            return new_marbles

    if marbles == 0:
        new_marbles = 0
        return new_marbles

def player_turn(marbles):

    if marbles != 0:
        print ("The pile has %i marbles in it" % marbles)
        max_to_take = int(marbles / 2)
        player_list = list(range(int(marbles / 2) + 1))
        player_list.remove(0)

        if max_to_take == 0:
            max_to_take = 1

        while True:
            try:
                player_query = int(input("How many marbles do you want to take? (%i, %i): " % (1, max_to_take)))
                if player_query in player_list:
                    new_marbles = marbles - player_query
                    return new_marbles
                if not player_list:
                    print ("Sorry, you lose.")
                    print ('')
                    new_marbles = 0
                    return new_marbles
                else:
                    print ('Value not within given range. Try again.')
                    print ('')
            except ValueError:
                print ('Query not understood. Try again.')
                print ('')

def nim():

    while True:
        query = input("Would you like to play now? (Y,N): ")

        if query.upper() == "Y":
            print ('')

            try:
                marbles = int(input("How many marbles are in the pile?: "))
                starting_player = input("Who will start? (P or C): ")

                if starting_player.upper() == "C":
                    while marbles > 0:
                        marbles = computer_turn(marbles)
                        marbles = player_turn(marbles)

                elif starting_player.upper() == "P":
                    while marbles > 0:
                        marbles = player_turn(marbles)
                        marbles = computer_turn(marbles)

                else:
                    print('Query not understood. Try again.')
                    print('')

            except ValueError:
                    print('Query not understood. Try again.')
                    print('')

        while query.upper() not in ("Y, N"):
            print('Query not understood. Try again.')
            print('')
            query = "Y"

        if query.upper() == 'N':
            print('Thank you for your time. Ending the program now')
            break

if __name__ == "__main__":

    nim()
