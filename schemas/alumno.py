from sqlalchemy import Column, Integer, String
from database import Base

class AlumnoS(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)