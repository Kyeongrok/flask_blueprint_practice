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

class Death(db.Model):
    __tablename__ = 'death'

    def __repr__(self):
        return f"Death('{self.person_id}', '{self.death_datetime}', '{self.death_type_concept_id}')"

    person_id = db.Column(db.Integer(), primary_key=True)
    death_date = db.Column(db.Date(), default=None)
    death_datetime = db.Column(db.DateTime(), default=None)
    death_type_concept_id = db.Column(db.Integer(), default=None)
    cause_concept_id = db.Column(db.Integer(), default=None)
    cause_source_value = db.Column(db.String(), default=None)
    cause_source_concept_id = db.Column(db.Integer(),default=None)

class VisitOccurrence(db.Model):
    __tablename__ = 'visit_occurrence'


    visit_occurrence_id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), default=None)
    visit_concept_id = db.Column(db.Integer(), default=None)
    visit_start_date = db.Column(db.Date(), default=None)
    visit_start_datetime = db.Column(db.DateTime(), default=None)
    visit_end_date = db.Column(db.Date(), default=None)
    visit_end_datetime = db.Column(db.DateTime(), default=None)
    visit_type_concept_id = db.Column(db.Integer(), default=None)
    provider_id = db.Column(db.Integer(), default=None)
    care_site_id = db.Column(db.Integer(), default=None)
    visit_source_value = db.Column(db.Integer(), default=None)
    visit_source_concept_id = db.Column(db.Integer(), default=None)
    admitting_source_concept_id = db.Column(db.Integer(), default=None)
    admitting_source_value = db.Column(db.String(), default=None)
    discharge_to_concept_id = db.Column(db.Integer(), default=None)
    discharge_to_source_value = db.Column(db.String(), default=None)
    preceding_visit_occurrence_id = db.Column(db.Integer(), default=None)
