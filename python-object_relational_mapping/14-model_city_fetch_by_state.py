#!/usr/bin/python3
"""
Fetches and displays all City objects from the database
along with their corresponding State names.
"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            dbName
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    session = Session()
    cityStates = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for city, state in cityStates:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    session.close()
