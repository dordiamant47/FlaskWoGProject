# Declare variables that will be in global scope
game_chosen = 0
game_difficulty = 0


def welcome(name):
    return f"""Hello {name} and welcome to the World of Games (WoG)
Here you can find many cool games to play"""


def load_game():
    print("""Please choose a game to play:
    1. Memory game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    global game_chosen
    game_chosen = input()

    # User input validation for game number - between 1-3
    while game_chosen not in {1, 2, 3}:
        try:
            game_chosen = int(game_chosen)
            if game_chosen not in {1, 2, 3}:
                raise ValueError
        except ValueError:
            print("Game number not valid, valid values: 1/2/3.\nPlease enter chosen game number: ")
            game_chosen = input()

    # User input validation for game difficulty - between 1-5
    print("Please choose game difficulty from 1 to 5: ")
    global game_difficulty
    game_difficulty = input()
    while game_difficulty not in {1, 2, 3, 4, 5}:
        try:
            game_difficulty = int(game_difficulty)
            if game_difficulty not in {1, 2, 3, 4, 5}:
                raise ValueError
        except ValueError:
            print("Game difficulty not valid, valid values: 1/2/3/4/5.\nPlease enter chosen game number: ")
            game_difficulty = input()
