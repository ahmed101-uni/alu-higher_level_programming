#!/usr/bin/python3
"""
Script that lists the id of a State object where name
matches the argument.
"""


from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    search = sys.argv[4]

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
    states = session.query(State).where(
        State.name == search
    ).order_by(State.id).all()

    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    session.close()

    session.close()
