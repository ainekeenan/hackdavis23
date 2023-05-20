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
    health = "give me the health"

    url = "https://api.edamam.com/api/recipes/v2?app_id=fd727a17&app_key=3db153f6a682953219a9bb02b92537f9&q={}&health={}".format(os.environ.get("Rare_Ingredients"), health)
    response = urllib.request.urlopen(url)
    recipes = response.read()
    dict = json.loads(recipes)

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

