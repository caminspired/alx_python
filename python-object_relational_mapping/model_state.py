"""this module contains the class State and an instance of class Base"""

if __name__ == "__main__":
    
    """importing attributes from SQLAlchemy"""
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    """initiating instance Base"""
    Base = declarative_base()

    """creating an empty class States that inherits from Base"""
    class State(Base):
        
        """
        Creates an empty class State in a database.

        Attributes:
        - id (int): The unique identifier for the state.
        - name (str): The name of the state.
        """
        
        __tablename__ = "states"
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)   
