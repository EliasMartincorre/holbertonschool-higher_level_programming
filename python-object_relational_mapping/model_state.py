# Import SQLAlchemy module
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()

# Define the State class
class State(Base):
    # Link to the MySQL table states
    __tablename__ = 'states'
    
    # Define the class attributes
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
