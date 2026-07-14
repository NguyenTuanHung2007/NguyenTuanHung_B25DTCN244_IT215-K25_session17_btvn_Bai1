from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas, services

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/packages/{package_id}", response_model=schemas.PackageResponse)
def get_package(package_id: int, db: Session = Depends(get_db)):
    return services.get_package_detail_service(db, package_id)

@app.post("/packages", response_model=schemas.PackageResponse, status_code=201)
def create_package(package_data: schemas.PackageBase, db: Session = Depends(get_db)):
    return services.create_package_service(db, package_data)

# Có thể thêm các API cho Warehouse, Waybill, Truck tương tự