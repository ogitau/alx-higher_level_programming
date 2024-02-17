#!/usr/bin/python3
"""prints all cities from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City

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
        new_st = State(name="California",
                       cities=[City(name="San Francisco")])
        session.add(new_st)
        session.commit()
