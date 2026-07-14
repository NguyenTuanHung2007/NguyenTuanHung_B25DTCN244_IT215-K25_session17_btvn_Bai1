from pydantic import BaseModel
from typing import List, Optional

class WaybillBase(BaseModel):
    tracking_number: str
    shipping_status: str

class WarehouseBase(BaseModel):
    warehouse_name: str
    location: str

class TruckBase(BaseModel):
    license_plate: str

class PackageBase(BaseModel):
    package_code: str
    weight: float
    warehouse_id: int

class PackageResponse(PackageBase):
    id: int
    warehouse: Optional[WarehouseBase]
    waybill: Optional[WaybillBase]
    trucks: List[TruckBase] = []

    class Config:
        from_attributes = True

class WaybillResponse(WaybillBase):
    id: int
    package_id: int
    class Config:
        from_attributes = True