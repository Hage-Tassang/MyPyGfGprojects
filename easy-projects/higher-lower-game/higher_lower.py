#Helps clear the previous output in the console
from IPython.display import clear_output
clear_output()

#import game files
from game_files import game_data as data
from game_files import game_ascii_graphics as art

#import random module for game logic and some randomness
import random as rndom


def higher_lower_game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = rndom.choice(data.data)
    account_b = rndom.choice(data.data)
    
    while game_should_continue:
        account_a = account_b
        account_b = rndom.choice(data.data)
        while account_a == account_b:
            account_b = rndom.choice(data.data)
        
        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(art.vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        
        is_correct = False
        if a_follower_count > b_follower_count:
            is_correct = guess == 'A'
        else:
            is_correct = guess == 'B'
        
        clear_output()
        print(art.logo)
        
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

higher_lower_game()