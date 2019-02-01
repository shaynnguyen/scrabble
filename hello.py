import lab11

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World'


@app.route('/scrabble/<myLetters>')
def show_make(myLetters):
    return repr(lab11.scrabbleWords(myLetters))

