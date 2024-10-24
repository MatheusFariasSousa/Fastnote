from app.db.connection import session


def get_conection():
    try:
        db_session = session()
        yield db_session

    finally:
        db_session.close()
