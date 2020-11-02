from flask import render_template, request, Blueprint
from flaskapp.models import Person

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    persons = Person.query.all()
    l = Person.query.filter_by(gender_concept_id=8507).all()
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return {'count':len(persons), 'male':len(l)}


@main.route("/about")
def about():
    return render_template('about.html', title='About')
