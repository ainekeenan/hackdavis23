from flask import Flask
import urllib.request, json, os

app = Flask(__name__)

@app.route("/CATS")

def hello_world():
    return "<p>Hello, World! CATSJKLSKLKLJSLSK</p>"

def from_url_get_otherRareRecipes():
    # request recipes with Rare ingredients variable
    #Recipes requested = 3
    # ignore common pantry items bc they are common
    url = "https://api.spoonacular.com/recipes/complexSearch?api_key =35a2e3a4aba74c3aaa99a943c2be1295 & includeIngredients={}&number=3&ignorePantry=true".format(os.environ.get("Rare_Ingredients"))
    response = urllib.request.urlopen(url)
    recipes = response.read()
    dict = json.load(recipes)

    # make empty array for recipes (can use recipes bc you loaded it into dict)
    recipes = []


    # get the title of recipes
    for recipe in dict[]{
        recipe = {
            "recipeName" = recipe["title"]
            "id" = recipe["id"]
        }
        recipes.append(recipe)

    }

    return {"results" : recipes}
    


if  __name__ == '__main__':
    app.run()

