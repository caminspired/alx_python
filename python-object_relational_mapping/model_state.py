"""this module contains the class State and an instance of class Base"""

if __name__ == "__main__":
    
    """importing attributes from SQLAlchemy"""
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    """initiating instance Base"""

    class State(Base):
        """creating class States that inherits from Base"""

        __tablename__ = "states"
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)   
