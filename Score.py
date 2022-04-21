import Utils
def add_score(difficulty):
    try:

        # If there is 'points of winning' in file read it
        f = open(Utils.scores_file_name, 'r')
        content = f.read()
        f.close()
        content = int(content) + difficulty * 3 + 5

    except FileNotFoundError:

        # If the file does not exist, create it and calculate the 'points of winning'
        f = open(Utils.scores_file_name, 'x')
        f.close()
        content = difficulty * 3 + 5

    finally:

        # Write 'points of winning' to file
        f = open(Utils.scores_file_name, 'w')
        f.write(str(content))
        f.close()
