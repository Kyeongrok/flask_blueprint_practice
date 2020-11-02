from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskapp import db


class Person(db.Model):
    __tablename__ = 'person'

    def __repr__(self):
        return '<Person %r>' % self.id

    person_id = db.Column(db.Integer(), primary_key=True) ##types.BIGINT(),
    gender_concept_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    year_of_birth = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    month_of_birth = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    day_of_birth = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    birth_datetime = db.Column(db.DateTime(), default=None) ##DateTime(),
    race_concept_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    ethnicity_concept_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    location_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    provider_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    care_site_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    person_source_value = db.Column(db.String(), default=None) ##types.VARCHAR(length=255),
    gender_source_value = db.Column(db.String(), default=None) ##types.VARCHAR(length=255),
    gender_source_concept_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    race_source_value = db.Column(db.String(), default=None) ##types.VARCHAR(length=50),
    race_source_concept_id = db.Column(db.Integer(), default=None) ##types.INTEGER(),
    ethnicity_source_value = db.Column(db.String(), default=None) ##types.VARCHAR(length=50),
    ethnicity_source_concept_id = db.Column(db.Integer(), default=None) ##types.INTEGER()})



