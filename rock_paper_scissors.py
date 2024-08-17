import random
round = 0
wins = 0

options = ['rock', 'paper', 'scissors']

print('Welcome to the Rock, Paper, Scissors game!!!')

user_name = input('Please Your Enter Name: ')

rounds  = input('How many rounds would you want to play? ')
while True:
    if rounds.isdigit():
        print('Let us begin, please note that 0 = rock, 1 = paper and 2 = scissors')
        rounds = int(rounds)
        break
    else: 
        print('Please enter a valid integer')
        rounds  = input('How many rounds would you want to play? ')
        continue
    
while rounds > round:
    player_choice = input('Which option are you choosing? Use either 0, 1, or 2. ')
    while True:
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if player_choice <= -1 or player_choice >= 3:
                print('Please choose an option between -1 and 3.')
                continue
            break
        else: 
            print('Please enter a valid integer')
            player_choice  = input('Which option are you choosing? Use either 0, 1, or 2. ')
            continue
    
    user_choice = options[player_choice]
    comp_choice = random.choice(options)
    print(comp_choice)
    print(user_choice)
    round += 1

    if user_choice == comp_choice:
        print('Damn...Its a tie!')
        if round <= 0: 
            round = 0
        else:
            round -= 1

    if player_choice == 0 and comp_choice == 'paper':
        print('The computer won!')
    
    if player_choice == 0 and comp_choice == 'scissors':
        print('You won!')
        wins += 1

    if player_choice == 1 and comp_choice == 'rock':
        print('You won!')
        wins += 1
    if player_choice == 1 and comp_choice == 'scissors':
        print('The computer won!')

    if player_choice == 2 and comp_choice == 'rock':
        print('The computer won!')

    if player_choice == 2 and comp_choice == 'paper':
        print('You won!')
        wins += 1

print(f'Congratulations {user_name}, you won {wins} out of {rounds}.')