from code.database.models import Raws


def get_raws(db):
    return db.query(Raws).all()