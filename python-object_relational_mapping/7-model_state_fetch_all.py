#this modules lists all states from a database
if __name__ == "__main__":
    
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    path = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                         .format(argv[1], argv[2], argv[3])
    
    session = sessionmaker(bind=path)
