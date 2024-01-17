# this module contains the class State and an instance of class Base
if __name__ == "__main__":
    
    # importing attributes from SQLAlchemy
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    
    # importing class Base
    Base = declarative_base()
    
    # creating class States that inherits from Base
    class State(Base):
        
        # defining method table that creates a table with properties 
        __tablename__ = "states"
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)   
