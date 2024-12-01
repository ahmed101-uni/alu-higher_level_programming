#!/usr/bin/python3
"""
Script that updates the name of the State object with
id 2 to "New Mexico".
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

    state = session.query(State).where(State.id == 2).one()
    state.name = "New Mexico"
    session.commit()

    session.close()
    session.close()
