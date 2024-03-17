#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a from the
Usage: ./13-model_state_delete_a.py     <mysql username>
                                        <mysql password>
                                        <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb:{}:{}@ocalhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(state).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()