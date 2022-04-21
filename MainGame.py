import os
import Live
import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Utils
import Score
import MainScores

print(Live.welcome('Guy'))
Live.load_game()
os.system(Utils.screen_cleaner)
if Live.game_chosen == 1:
    MemoryGame.play(Live.game_difficulty)
elif Live.game_chosen == 2:
    GuessGame.play(Live.game_difficulty)

# Doesn't need to validate the game chosen because the Live module checks that
else:
    CurrencyRouletteGame.play(Live.game_difficulty)

if MemoryGame.win or GuessGame.win or CurrencyRouletteGame.win:
    Score.add_score(Live.game_difficulty)

MainScores.score_server()
