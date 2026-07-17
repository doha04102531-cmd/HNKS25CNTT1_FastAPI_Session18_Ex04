from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import services
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hệ thống Quản lý Đăng ký Workshop Sinh viên",
    description="Hệ thống API quản lý thông tin sinh viên, workshop và quy trình đăng ký lớp học ngắn hạn.",
    version="1.0.0"
)


@app.post("/students", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return services.create_student(db=db, student=student)


@app.get("/students", response_model=List[schemas.StudentResponse])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_students(db, skip=skip, limit=limit)


@app.post("/workshops", response_model=schemas.WorkshopResponse, status_code=status.HTTP_201_CREATED)
def create_workshop(workshop: schemas.WorkshopCreate, db: Session = Depends(get_db)):
    return services.create_workshop(db=db, workshop=workshop)


@app.get("/workshops", response_model=List[schemas.WorkshopResponse])
def read_workshops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_workshops(db, skip=skip, limit=limit)


@app.get("/workshops/{id}", response_model=schemas.WorkshopResponse)
def read_workshop(id: int, db: Session = Depends(get_db)):
    return services.get_workshop_by_id(db, workshop_id=id)


@app.post("/registrations", response_model=schemas.RegistrationResponse, status_code=status.HTTP_201_CREATED)
def register_workshop(registration: schemas.RegistrationCreate, db: Session = Depends(get_db)):
    return services.register_workshop(db=db, reg_data=registration)


@app.get("/students/{id}/workshops", response_model=List[schemas.WorkshopResponse])
def get_student_workshops(id: int, db: Session = Depends(get_db)):
    return services.get_workshops_by_student(db, student_id=id)

@app.get("/workshops/{id}/students", response_model=List[schemas.StudentResponse])
def get_workshop_students(id: int, db: Session = Depends(get_db)):
    return services.get_students_by_workshop(db, workshop_id=id)


@app.put("/registrations/{id}/cancel", response_model=schemas.RegistrationResponse)
def cancel_registration(id: int, db: Session = Depends(get_db)):
    return services.cancel_registration(db, registration_id=id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
