#!/usr/bin/python3
"""
Adds a new State object "Louisiana" to the database and
prints its id.
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
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print(newState.id)

    session.close()
    session.close()
