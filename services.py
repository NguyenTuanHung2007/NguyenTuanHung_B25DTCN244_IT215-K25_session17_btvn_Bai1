from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Package, Warehouse, Waybill, Truck
from schemas import PackageBase

def get_package_detail_service(db: Session, package_id: int):
    package = db.query(Package).filter(Package.id == package_id).first()
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

def create_package_service(db: Session, package_data: PackageBase):
    warehouse = db.query(Warehouse).filter(Warehouse.id == package_data.warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    
    new_package = Package(**package_data.model_dump())
    try:
        db.add(new_package)
        db.commit()
        db.refresh(new_package)
        return new_package
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Mã kiện hàng đã tồn tại")