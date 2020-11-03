from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskapp import db


class Person(db.Model):
    __tablename__ = 'person'

    def __repr__(self):
        return f"Person('{self.person_id}', '{self.birth_datetime}', '{self.race_concept_id}', '{self.ethnicity_concept_id}')"

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



class Concept(db.Model):
    __tablename__ = 'concept'

    def __repr__(self):
        return f"Concept('{self.concept_id}', '{self.concept_name}', '{self.concept_code}')"

    concept_id = db.Column(db.Integer(), primary_key=True)  #INTEGER(),
    concept_name = db.Column(db.String(), default=None)  #VARCHAR(length=255),
    domain_id = db.Column(db.String(), default=None)  #VARCHAR(length=50),
    vocabulary_id = db.Column(db.String(), default=None)  #VARCHAR(length=50),
    concept_class_id = db.Column(db.String(), default=None)  #VARCHAR(length=50),
    standard_concept = db.Column(db.String(), default=None)  #VARCHAR(length=20),
    concept_code = db.Column(db.Integer(), default=None)  #INTEGER(),
    valid_start_date = db.Column(db.Date(), default=None)  #Date(),
    valid_end_date = db.Column(db.Date(), default=None)  #Date(),
    invalid_reason = db.Column(db.String(), default=None)  #VARCHAR(length=20)