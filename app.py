from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import urllib.request, json
import cgi, cgitb

app = Flask(__name__)

forms=cgi.FieldStorage()

def from_url_get_otherRareRecipes(diet, ingredients):
    # request recipes with Rare ingredients variable
    #Recipes requested = 3
    # ignore common pantry items bc they are common
    ingredients = "apple"

    # url = "https://api.edamam.com/api/recipes/v2?app_id=fd727a17&app_key=3db153f6a682953219a9bb02b92537f9&q={}&health={}&type=any".format(os.environ.get("Rare_Ingredients"), health)
    url = "https://api.edamam.com/api/recipes/v2?app_id=fd727a17&app_key=3db153f6a682953219a9bb02b92537f9&q={ingredients}&health={health}&type=any".format(ingredients=ingredients, health=diet)
    if diet == 'none':
        url = "https://api.edamam.com/api/recipes/v2?app_id=fd727a17&app_key=3db153f6a682953219a9bb02b92537f9&q={ingredients}&type=any".format(ingredients=ingredients)
    response = urllib.request.urlopen(url)   
    recipes = response.read()
    dict = json.loads(recipes)

    # make empty array for recipes (can use recipes bc you loaded it into dict)
    recipes = []


    # get the title of recipes
    for recipe in dict["hits"]:
        print(recipe["recipe"]["ingredientLines"])
        recipe = {
          "recipeName" : recipe["recipe"]["label"],
           "urlLink" : recipe["recipe"]["url"],
           "ingredients": recipe["recipe"]["ingredients"],
        }
        recipes.append(recipe)

    
    return recipes
    #return "<p>" + str(recipes) +  "</p>"


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        url = request.form.get("url")

        if url:
            response = requests.get(url)
            diet = request.form.get("dietary-restriction")

            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            ingredient_elements = soup.find_all(class_ = lambda c: c and "ingredient" in c.lower())
            ingredients = [element.get_text(strip=True)+"," for element in ingredient_elements]

            if ingredients:
                print(diet)
                recipes = from_url_get_otherRareRecipes(diet, ingredients)
                return render_template('result.html', recipes = recipes)

        return render_template('invalid.html')

if __name__ == '__main__':
    app.run()
