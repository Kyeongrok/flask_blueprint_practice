from flask import render_template, request, Blueprint
from sqlalchemy import func
from flaskapp.models import Person, Concept, db
from flaskapp.utils import get_concepts
from flask_restplus import Api, Resource, Namespace

main = Namespace('main', description='main')

@main.route("/home")
class PersonApi(Resource):
    def get(self):
        '''
        persons
        visit_occurrence
        condition_occurrence
        drug_exposure
        death
        :return:
        '''
        d_concept = get_concepts(Person.gender_concept_id)

        gr = Person.query\
            .with_entities(Person.gender_concept_id, func.count(Person.gender_concept_id).label('count'))\
            .group_by(Person.gender_concept_id)\
            .all()
        l = []
        for row in gr:
            r = row._asdict()
            r['concept_name'] = d_concept[r['gender_concept_id']]
            l.append(r)
        # return render_template('statistics.html', gr = l)
        return {'Data':l}

@main.route("/about")
def about():
    return render_template('about.html', title='About')
