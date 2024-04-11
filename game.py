import random

def game():
    player_choice = input('Choose rock, paper, or scissors: ').lower()
    computer_number = random.randint(1, 3)
    computer_choice = ''

    if computer_number == 1:
        computer_choice = 'rock'
    elif computer_number == 2:
        computer_choice = 'paper'
    elif computer_number == 3:
        computer_choice = 'scissors'

    winner = ''
    if player_choice in ['rock', 'paper', 'scissors']:
        if (player_choice == 'rock' and computer_choice == 'scissors') or \
           (player_choice == 'paper' and computer_choice == 'rock') or \
           (player_choice == 'scissors' and computer_choice == 'paper'):
            winner = 'You'
        elif player_choice == computer_choice:
            winner = "It's a tie!"
        else:
            winner = 'The computer'
        print()
        print('You chose ' + player_choice + '.')
        print('The computer chose ' + computer_choice + '.')
        print()
        print(winner + ' won!')
    else:
        print("You did not choose rock, paper, or scissors, try again.")
        game()
        return
    print("Do you want to play again? (Y/N)")
    playagain = input()
    if(playagain.lower() == 'y'):
        game()
game()
