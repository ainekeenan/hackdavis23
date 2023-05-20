from flask import Flask, render_template, request
import cgi, cgitb

app = Flask(__name__)

forms=cgi.FieldStorage()
recipe_url = ""


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        recipe_url = request.form.get("url")
        print(recipe_url)
    return render_template('home.html', url=recipe_url)

if __name__ == '__main__':
    app.run()


