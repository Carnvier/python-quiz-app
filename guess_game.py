import random
guesses =  0
user_num = input('Type in a randomm number: ')

user_num = int(user_num)
random = random.randint(0, user_num)


while True:
    guesses += 1
    guess = int(input('Guess the number: '))
    
    if guess == random:
        print(f'Congratulations! You guessed the number in {guesses} attempts.')
        break
    elif guess < random:
        print('Too low, try again.')

    else:
        print('Too high, try again.')
    continue
