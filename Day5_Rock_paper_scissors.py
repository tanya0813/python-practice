import random

options = ('rock', 'paper', 'scissors')

player= None
computer= random.choice(options)

while player not in options:
    player= input('Enter your choice: ')

print (f'Player: {player}')
print (f'Computer: {computer}')

if player==computer:
    print("It's a tie!")

if player=='rock' and computer=='scissors':
    print("You won!")

if player=='rock' and computer=='paper':
    print("You lose!")

if player=='scissors' and computer=='paper':
    print("You win!")

if player=='scissors' and computer=='rock':
    print("You lose!")

if player=='paper' and computer=='scissors':
    print("You lose!")

if player=='paper' and computer=='rock':
    print("You win!")
