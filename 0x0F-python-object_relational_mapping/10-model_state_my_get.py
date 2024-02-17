#!/usr/bin/python3
"""lists the States from the database as indicated by the user"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    
    username, password, database, state = argv[1], argv[2], argv[3], argv[4]
    host = "localhost"
    port = "3306"
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        st_name = session.query(State).filter_by(name=state).first()
        if st_name:
            print(f"{st_name.id}")
        else:
            print("Not found")
