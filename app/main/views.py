from flask import render_template
from . import main
import pdb
from ..models import Review, Recipe, User, GroceryList

@main.route("/")
def home():
    return render_template('index.html')

@main.route("/review")
def review():
    pdb.run

    
    header = []
    description = []
    rating = []
    #recipeid = Review.recipeid
    return render_template('review.html')
