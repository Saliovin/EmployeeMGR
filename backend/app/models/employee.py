from sqlalchemy import JSON, Column, Integer, String
from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    employee_type = Column(String)
    properties = Column(JSON)
