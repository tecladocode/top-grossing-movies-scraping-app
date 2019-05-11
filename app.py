from flask import Flask, render_template
from moviedata import get_top_grossing


app = Flask(__name__)
movies = [
    {"name": "Avatar", "grossing": "$2,788,000,000", "year": "2009"},
    {"name": "Avengers: Endgame", "grossing": "$2,320,700,000", "year": "2019"},
    {"name": "Titanic", "grossing": "$2,187,500,000", "year": "1997"},
    {
        "name": "Star Wars: The Force Awakens",
        "grossing": "$2,068,200,000",
        "year": "2015",
    },
    {"name": "Avengers: Infinity War", "grossing": "$2,048,400,000", "year": "2018"},
    {"name": "Jurassic World", "grossing": "$1,671,700,000", "year": "2015"},
    {"name": "Marvel's The Avengers", "grossing": "$1,518,800,000", "year": "2012"},
]


@app.route("/")
def home():
    return render_template("index.html", movies=get_top_grossing())

