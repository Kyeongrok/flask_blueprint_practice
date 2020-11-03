from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp.models import Person

person = Blueprint('person', __name__, url_prefix='/person')

@person.route('/', methods=["GET"])
@person.route('/<int:page>')
def idx(page):
    persons = Person.query.paginate(page=page, per_page=10)
    return render_template('person_list.html', persons=persons)


@person.route("/list/<int:page_no>", methods=['GET', 'POST'])
@person.route("/list", methods=['GET', 'POST'])
def list():
    # 환자 정보를 출력하고 paging한다.
    return render_template('register.html', title='Register')

