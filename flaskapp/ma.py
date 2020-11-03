#
# from flask_restful import Resource, Api
# from flask_restful_swagger import swagger
# from flaskapp.utils import get_concepts
# from flaskapp.models import Person
# from sqlalchemy import func
#
# class MyApi(Resource):
#     @swagger.model
#     @swagger.operation(notes='hello')
#     def get(self, ff):
#         d_concept = get_concepts(Person.gender_concept_id)
#
#         gr = Person.query \
#             .with_entities(Person.gender_concept_id, func.count(Person.gender_concept_id).label('count')) \
#             .group_by(Person.gender_concept_id) \
#             .all()
#         l = []
#         for row in gr:
#             r = row._asdict()
#             r['concept_name'] = d_concept[r['gender_concept_id']]
#             l.append(r)
#         return {'Response':200, 'Data':l}
