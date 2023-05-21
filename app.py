from flask import Flask
import urllib.request, json

import os

app = Flask(__name__)

@app.route("/CATS")
def from_url_get_otherRareRecipes():
    # request recipes with Rare ingredients variable
    #Recipes requested = 3
    # ignore common pantry items bc they are common

    #rare ingredients, NO SPACES to work on aine computer
    ingredients = "give me the rate ingredients"
    # restrictions we have
    health = "give me the health"

    # url = "https://api.edamam.com/api/recipes/v2?app_id=fd727a17&app_key=3db153f6a682953219a9bb02b92537f9&q={}&health={}&type=any".format(os.environ.get("Rare_Ingredients"), health)
    url = "https://api.edamam.com/api/recipes/v2?app_id=fd727a17&app_key=3db153f6a682953219a9bb02b92537f9&q=chicken,pasta&health=kosher&type=any"
    response = urllib.request.urlopen(url)   
    recipes = response.read()
    dict = json.loads(recipes)

    # make empty array for recipes (can use recipes bc you loaded it into dict)
    recipes = []


    # get the title of recipes
    for recipe in dict["hits"]:
        recipe = {
          "recipeName" : recipe["recipe"]["label"],
           "urlLink" : recipe["recipe"]["url"]
        }
        recipes.append(recipe)

    
   return recipes
   # return "<p>" + str(recipes) +  "</p>"
    


if  __name__ == '__main__':
    app.run()

