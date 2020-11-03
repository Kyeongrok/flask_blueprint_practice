from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp.models import Person

concept = Blueprint('concept', __name__, url_prefix='/concept')

@concept.route('/', methods=["GET"])
@concept.route('/<int:page>')
def idx(page):
    concepts = Person.query.paginate(page=page, per_page=10)
    return render_template('concept_list.html', concepts=concepts)


@concept.route("/list/<int:page_no>", methods=['GET', 'POST'])
@concept.route("/list", methods=['GET', 'POST'])
def list():
    # 환자 정보를 출력하고 paging한다.
    return render_template('register.html', title='Register')

