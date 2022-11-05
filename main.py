from flask import Flask, render_template
from utils import get_all
from utils import get_man
from utils import get_candidate_by_name
from utils import get_candidate_by_skill

# http://127.0.0.1:5000/
app = Flask(__name__)


@app.route("/")
def main_page():
    people = get_all()
    return render_template("list.html", people=people)


@app.route('/people/<int:pk>')
def man_page(pk):
    man = get_man(pk)
    return render_template("single.html", man=man)


@app.route("/people/<skill>")
def search_skill(skill):
    man = get_candidate_by_skill(skill)
    return render_template("skill.html", man=man, skill=skill)


@app.route('/search/<name>')
def search_man(name):
    man = get_candidate_by_name(name)
    return render_template("search.html", man=man)


app.run()
