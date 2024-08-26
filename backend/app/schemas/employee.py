import json
from pydantic import BaseModel, EmailStr, field_validator


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    employee_type: str
    properties: dict

    @field_validator("properties", mode="before")
    @classmethod
    def parse_properties(cls, value):
        if isinstance(value, str):
            return json.loads(value)
        return value


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
