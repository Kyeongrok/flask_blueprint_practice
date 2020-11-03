from flaskapp.models import Person, Death, VisitOccurrence, db
from flask_restplus import Api, Resource, Namespace
from flaskapp.utils import get_concepts

concept = Namespace('concept', description='각 Table에 사용된 concept 정보를 검색합니다.')

@concept.route("/person")
class ConceptPerson(Resource):
    def get(self):
        '''
        Person table의 concept_id와 concept_name을 조회 합니다.

        Person table에는 아래와 같이 6가지 concept_id가 있습니다.
        gender_concept_id
        race_concept_id
        ethnicity_concept_id
        gender_source_concept_id
        race_source_concept_id
        ethnicity_source_concept_id

        :return: dict
        '''
        return {
            'Description': 'Person에 대한 concept_id 자료',
            'Data':{
                'd_gender_concept' : get_concepts(Person.gender_concept_id),
                'd_race_concept' : get_concepts(Person.race_concept_id),
                'd_ethnicity_concept' : get_concepts(Person.ethnicity_concept_id),
                'd_race_source_concept' : get_concepts(Person.race_source_concept_id),
                'd_ethnicity_source_concept' : get_concepts(Person.ethnicity_source_concept_id),
                'd_gender_source_concept' : get_concepts(Person.gender_source_concept_id),
            }
        }
@concept.route("/visit_occurrence")
class ConceptVisit(Resource):
    def get(self):
        '''
        visit_occurrence table의 concept_id와 concept_name을 조회 합니다.

        visit_occurrence table에는 아래와 같이 5가지 concept_id가 있습니다.
        visit_concept_id
        visit_type_concept_id
        visit_source_concept_id
        admitting_source_concept_id
        discharge_to_concept_id

        :return: dict
        '''
        return {
            'Description': 'Visit에 대한 concept_id 자료',
            'Data':{
                'visit_concept_id': get_concepts(VisitOccurrence.visit_concept_id),
                'visit_type_concept_id': get_concepts(VisitOccurrence.visit_type_concept_id),
                'visit_source_concept_id': get_concepts(VisitOccurrence.visit_source_concept_id),
                'admitting_source_concept_id': get_concepts(VisitOccurrence.admitting_source_concept_id),
                'discharge_to_concept_id': get_concepts(VisitOccurrence.discharge_to_concept_id),
            }
        }