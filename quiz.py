score =  0
questions = ['Who is the current president of Zimbabwe (PLEASE ENTER NAME ONLY) ', 
             'Where do we find the biggest peak in Zimbabwe? ', 
             'What is our local language as Zimbabweans? ', 
             'How many seasons do we have in Zimbabwe? ', 
             'Where do we find MOSIA-TUNYA? '  ]
count = 0
answers = ['EMMERSON MNANGAGWA',
           'NYANGA', 
           'shona', 
           'four', 
           'VICTORIAL FALLS']
answer =  ''
print('Hello welcome to our quiz game')

confirm = input('Would you want to play the game? (y/n): ')

if confirm == 'y':
    print('Let us start!')
    for items in questions:
        answer = input(questions[count])
        
        if answer.upper() == answers[count].upper():
            print('Correct!')
            score += 1
            count += 1
        else:
            print('Wrong answer')
            count += 1
            print(answers.upper())

    print(f'Well done your scored {score} points! Out of {str(count)}')
    print(f'You got {(score / count)*100}%')

else:
    print('Thank you for joining the game')
    quit()