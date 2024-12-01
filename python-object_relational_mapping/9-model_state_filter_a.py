#!/usr/bin/python3
"""
Script that lists all State objects from the database
that contain the letter 'a' in their name, ordered
by state id.
"""


from sqlalchemy import create_engine
from model_state import Base, State
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
    for state in session.query(State).where(
        State.name.like("%a%")
    ).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()

    session.close()
