from sqlalchemy import func
from flaskapp.models import Person, Death, VisitOccurrence, db
from flaskapp.utils import get_concepts
from flask_restplus import Api, Resource, Namespace

statistics = Namespace('statistics', description='Table의 통계를 보여줍니다.')

@statistics.route("/person")
class StatisticsPerson(Resource):
    def get(self):
        '''
        person table의 통계를 보여줍니다.
        전체 환자 수
        성별 환자 수
        인종별 환자 수
        민족별 환자 수
        사망 환자 수
        :return: dict
        '''
        # return render_template('statistics.html', gr = l)
        l_gender = count_by_model_concept_id(Person, Person.gender_concept_id, 'gender_concept_id')
        #ethnicity의 모든 concept_id value는 0이기 때문에 source_value로 하였습니다.
        l_ethnicity = person_by_source_value(Person.ethnicity_source_value)
        l_race = count_by_model_concept_id(Person, Person.race_concept_id, 'race_concept_id')
        i_person = db.session.query(Person).count()
        i_death = db.session.query(Death).count()
        return {
            'Description':'Person에 대한 통계 자료',
            'Data':{
                'person_total_cnt':i_person,
                'death_total_cnt':i_death,
                'gender':l_gender, 'ethnicity':l_ethnicity, 'race':l_race}
        }


@statistics.route("/visit_occurrence")
class StatisticsPerson(Resource):
    def get(self):
        '''
        visit(방문) Talbe의 통계를 보여줍니다.
        방문 유형(입원/외래/응급)별 방문 수
        성별 방문 수
        인종별 환자 수
        민족별 환자 수
        방문시 연령대(10세 단위)별 환자 수
        :return: dict
        '''
        l_visit_type = count_by_model_concept_id(VisitOccurrence, VisitOccurrence.visit_concept_id, 'visit_concept_id')
        l_visit_by_gender = visit_by_concept(Person.gender_concept_id, 'gender_concept_id')
        l_visit_by_ethnicity = visit_by_value('ethnicity_source_value')
        l_visit_by_race = visit_by_concept(Person.race_concept_id, 'race_concept_id')
        l_visit_by_age = visit_by_age_range()
        return {
            'Description':'환자가 방문한 내역',
            'Data':{
                'visit_type':l_visit_type,
                'visit_by_gender':l_visit_by_gender,
                'visit_by_ethnicity':l_visit_by_ethnicity,
                'visit_by_race':l_visit_by_race,
                'visit_by_age':{
                    '0=<age<10':l_visit_by_age[0],
                    '10=<age<20':l_visit_by_age[1],
                    '20=<age<30':l_visit_by_age[2],
                    '30=<age<40':l_visit_by_age[3],
                    '40=<age<50':l_visit_by_age[4],
                    '50=<age<60':l_visit_by_age[5],
                    '60=<age<70':l_visit_by_age[6],
                    '70=<age<80':l_visit_by_age[7],
                    '80=<age':l_visit_by_age[8]
                }
            }
        }
def count_by_model_concept_id(model, model_concept_id, column_name):
    d_concept = get_concepts(model_concept_id)
    gr = model.query \
        .with_entities(model_concept_id, func.count(model_concept_id).label('count')) \
        .group_by(model_concept_id) \
        .all()
    l = []
    for row in gr:
        r = row._asdict()
        r['concept_name'] = d_concept[r[column_name]]
        l.append(r)
    return l

def person_by_source_value(model_source_value):
    gr = Person.query \
        .with_entities(model_source_value, func.count(model_source_value).label('count')) \
        .group_by(model_source_value) \
        .all()

    return [row._asdict() for row in gr]

def visit_by_concept(model_concept_id, concept_column_name):
    d_concept = get_concepts(model_concept_id)
    result = db.engine.execute('''
            SELECT v.{} AS c1, COUNT(v.{}) AS COUNT 
            FROM(
                SELECT visit_occurrence.visit_concept_id, person_1.{} 
                FROM visit_occurrence JOIN person AS person_1 ON visit_occurrence.person_id = person_1.person_id) AS v 
                GROUP BY c1;'''.format(concept_column_name, concept_column_name, concept_column_name))
    l = []
    for r in result:
        l.append({'gender':d_concept[r[0]], 'count':r[1]})
    return l

def visit_by_value(concept_column_name):
    result = db.engine.execute('''
            SELECT v.{} AS c1, COUNT(v.{}) AS COUNT 
            FROM(
                SELECT visit_occurrence.visit_concept_id, person_1.{} 
                FROM visit_occurrence JOIN person AS person_1 ON visit_occurrence.person_id = person_1.person_id) AS v 
                GROUP BY c1;'''.format(concept_column_name, concept_column_name, concept_column_name))
    l = []
    for r in result:
        l.append({'gender':r[0], 'count':r[1]})
    return l

def visit_by_age_range():
    result = db.engine.execute('''
    select
      sum(case when date_part('year', AGE(p1.birth_datetime))<10 then 1 end) as "age<10",
      sum(case when date_part('year', age(p1.birth_datetime))>=10 and date_part('year', AGE(p1.birth_datetime))<20 then 1 end) as "10<age<20",
      sum(case when date_part('year', age(p1.birth_datetime))>=20 and date_part('year', age(p1.birth_datetime))<30 then 1 end) AS "20<age<30",
      sum(case when date_part('year', age(p1.birth_datetime))>=30 and date_part('year', age(p1.birth_datetime))<40 then 1 end) AS "30<age<40",
      sum(case when date_part('year', age(p1.birth_datetime))>=40 and date_part('year', age(p1.birth_datetime))<50 then 1 end) AS "40<age<50",
      sum(case when date_part('year', age(p1.birth_datetime))>=50 and date_part('year', age(p1.birth_datetime))<60 then 1 end) AS "50<age<60",
      sum(case when date_part('year', AGE(p1.birth_datetime))>=60 and date_part('year', age(p1.birth_datetime))<70 then 1 end) AS "60<age<70",  
      sum(case when date_part('year', AGE(p1.birth_datetime))>=70 and date_part('year', age(p1.birth_datetime))<80 then 1 end) AS "70<age<80",  
      sum(case when date_part('year', AGE(p1.birth_datetime))>=80 then 1 end) AS "70<age"
    from
      visit_occurrence
    INNER JOIN person AS p1 ON visit_occurrence.person_id = p1.person_id
    ''')

    for r in result:
        return list(r)

