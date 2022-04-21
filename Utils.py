import os

scores_file_name = 'Scores.txt'
bad_return_code = 408
if os.name == 'nt':
    screen_cleaner = 'cls'
else:
    screen_cleaner = 'clear'
