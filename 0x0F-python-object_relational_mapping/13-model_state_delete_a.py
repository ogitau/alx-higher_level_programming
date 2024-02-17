#!/usr/bin/python3
"""Deletes the States from the database as indicated id by the user"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    username, password, database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = "3306"
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        delete_state = session.query(State).filter(
            State.name.contains('a')).all()
        if delete_state:
            for state in delete_state:
                session.delete(state)
            session.commit()
