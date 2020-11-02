from flask import render_template, url_for, flash, redirect, request, Blueprint

person = Blueprint('person', __name__, url_prefix='/person')

@person.route("/", methods=['GET', 'POST'])
def idx():
    return 'person'


@person.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Register')

