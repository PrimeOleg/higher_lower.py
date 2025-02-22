# importing all modules that will be needed for performance of the task
import random
import art
from game_data import data

def data_generator():
    """Generation of data taking a random int and accessing the data in a list on concept of list[0]..., -1 done to stay in range of the list"""
    account = random.randint(0, len(data) - 1)
    return data[account]

def answer(d_a, d_b):
    """Function that will check for the right answer based on the account's follower count"""
    if d_a['follower_count'] > d_b['follower_count']:
        return "A"
    elif d_a['follower_count'] < d_b['follower_count']:
        return "B"

def replay():
    """Replay function allowing user to restart the game whenever they want"""
    if input("\nDo you want to play again? 'Y' or 'N': ").upper() == "Y":
        game()

def game():
    """A main game function that will work based off the checks performed by other functions"""
    score = 0
    game_over = False
    data_a = data_generator()
    data_b = data_generator()

    print(art.logo)
    while not game_over:

        while data_a == data_b:  # check if both of datasets are equal to each other in which case regenerate data
            data_a = data_generator()

        correct_answer = answer(data_a, data_b)
        print(correct_answer)
        print(f"Compare A: {data_a['name']} a {data_a['description']} from {data_a['country']}")
        print(art.vs)
        print(f"Compare B: {data_b['name']} a {data_b['description']} from {data_b['country']}")
        guess = input("Guess who has more followers? 'A' or 'B': ").upper()

        if guess == correct_answer:
            score += 1
            print("\n" * 20)
            print(f"Correct! You got {score} points.")
            data_a = data_b
            data_b = data_generator()

        else:
            game_over = True
            print("\n" * 20)
            print(f"Wrong! Your final score was {score}.")
            print(art.game_over)
            replay()
game()
