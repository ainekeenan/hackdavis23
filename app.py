from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import cgi, cgitb

app = Flask(__name__)

forms=cgi.FieldStorage()


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        url = request.form.get("url")

        if url:
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            ingredient_elements = soup.find_all(class_ = lambda c: c and "ingredient" in c.lower())
            ingredients = [element.get_text(strip=True)+"," for element in ingredient_elements]
            
            if ingredients:
                return ingredients

        return render_template('invalid.html')

if __name__ == '__main__':
    app.run()


