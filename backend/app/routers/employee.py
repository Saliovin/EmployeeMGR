import app.schemas.employee as schemas
import app.crud.employee as crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])


@router.post("/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@router.get("/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@router.get("/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_employee


@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int, employee: schemas.EmployeeBase, db: Session = Depends(get_db)
):
    db_employee = crud.update_employee(db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_employee


@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db, employee_id=employee_id)
    return {"message": "Item deleted successfully"}
