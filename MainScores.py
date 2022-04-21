import Utils
from flask import Flask
import os
score = ''

app = Flask(__name__)
@app.route('/')
def score_server():
    global score
    try:
        f = open(Utils.scores_file_name, 'r')
        score = f.read()
        f.close()
        return f'''<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is <div id="score">{score}</div></h1>
    </body>
</html>'''
    except OSError as exception:
        return f'''<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <body>
    <h1><div id="score" style="color:red">{exception}</div></h1>
    </body>
    </html>'''
    
    finally:
#        os.system("export FLASK_APP=MainScores.py")
        app.run(debug=False,host='0.0.0.0')
