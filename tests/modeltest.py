""""id": 9,
    "title": "Marinated Fresh Anchovies: Alici Marinate",
    "readyInMinutes": 420,
    "servings": 8,
    "sourceUrl": "http://www.foodnetwork.com/recipes/mario-batali/marinated-fresh-anchovies-alici-marinate-recipe/index.html",
    "image": "https://spoonacular.com/recipeImages/9-556x370.jpeg",
    "imageType": "jpeg",
    "summary": "Marinated Fresh Anchovies: Alici Marinate requires approximately <b>7 hours</b> from start to finish. This recipe makes 8 servings with <b>269 calories</b>, <b>24g of protein</b>, and <b>17g of fat</b> each. For <b>$5.5 per serving</b>, this recipe <b>covers 22%</b> of your daily requirements of vitamins and minerals. 7 people have tried and liked this recipe. If you have anchovies, garlic, oregano, and a few other ingredients on hand, you can make it. It is brought to you by Foodnetwork. It works well as a pricey main course. It is a good option if you're following a <b>gluten free, dairy free, paleolithic, and primal</b> diet. Taking all factors into account, this recipe <b>earns a spoonacular score of 82%</b>, which is excellent. <a href=\"https://spoonacular.com/recipes/fresh-anchovies-marinated-in-salsa-verde-647\">Fresh Anchovies Marinated In Salsa Verde</a>, <a href=\"https://spoonacular.com/recipes/carote-marinate-marinated-carrots-481292\">Carote marinate (Marinated Carrots)</a>, and <a href=\"https://spoonacular.com/recipes/marinated-anchovies-253536\">Marinated Anchovies</a> are very similar to this recipe.",
    "cuisines": [],
    "dishTypes": [
        "lunch",
        "main course",
        "main dish",
        "dinner"
    ],
    "diets": [
        "gluten free",
        "dairy free",
        "paleolithic",
        "primal",
        "whole 30",
        "pescatarian"
    ],
    "occasions": [],
    "winePairing": {
        "pairedWines": [
            "sauvignon blanc",
            "riesling",
            "sparkling rose"
        ],
        "pairingText": "Anchovies can be paired with Sauvignon Blanc, Riesling, and Sparkling rosé. In general, crisp white wines and sparkling wine pair well with strongly flavored, oily fish. One wine you could try is Pedroncelli East Side Vineyard Sauvignon Blanc. It has 4.5 out of 5 stars and a bottle costs about 14 dollars.",
        "productMatches": [
            {
                "id": 435994,
                "title": "Pedroncelli East Side Vineyard Sauvignon Blanc",
                """

#
#
#
#This is response in json format from spoon.


import unittest
import pdb
#pdb.run
from app.models import Recipe, Review, GroceryList, User

class Recipe(unittest.TestCase):
    def setUp(self) -> None:
        self.new_recipe_created = Recipe('32','Prezelz','image','put together ingredients','combine in pot and cook for eighty minutes')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_recipe_created,Recipe))
