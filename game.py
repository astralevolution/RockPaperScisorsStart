import random


player_choice = input('Do you want rock, paper, or scisors?').lower()
computer_number = random.randint(1,3)
computer_choice = ''

# Computer number is either one, two or three

if computer_number == 1:
    # Make computer_choice rock
    # Delete pass when you add some code
    pass

elif computer_number == 2:
    # Make computer_choice paper
    # Delete pass when you add some code
    pass

elif computer_number == 3:
    # Make computer_choice scisors
    # Delete pass when you add some code
    pass

winner = ''
if player_choice == 'rock':
    # Decide who won and store it in winner
    # Delete pass when you add some code
    pass
elif player_choice == 'paper':
    # Decide who won and store it in winner
    # Delete pass when you add some code
    pass
elif player_choice == 'scissors':
    # Decide who won and store it in winner
    # Delete pass when you add some code
    pass




print('You chose: ' + ' ' + player_choice)
print('The computer chose' + ' ' + computer_choice)
print('The ' + winner + ' won!')

