from flaskapp.models import Concept, db
def get_concepts(model_concept_id):

    query = db.session.query(model_concept_id.distinct())
    concept_ids = [row[0] for row in query.all()]
    result = db.session.query(Concept).filter(Concept.concept_id.in_(concept_ids)).all()
    d = {}
    for item in result:
        if d.get(item.concept_id) == None:
            d[item.concept_id] = ''
        d[item.concept_id] = item.concept_name
    return d