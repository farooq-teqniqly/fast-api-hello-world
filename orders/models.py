from datetime import datetime
from enum import Enum
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, conlist, conint, field_validator


class Size(Enum):
    small = "small",
    medium = "medium",
    large = "large"


class Status(Enum):
    created = "created",
    in_progress = "in_progress",
    cancelled = "cancelled",
    dispatched = "dispatched",
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1

    @field_validator("quantity")
    @classmethod
    def ensure_quantity_non_nullable(cls, value: int) -> int:
        if value is None:
            raise ValueError("Assign a value to Quantity.")

        return value


class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_length=1)


class GetOrderSchema(BaseModel):
    id: UUID
    created: datetime
    status: Status
    items: conlist(OrderItemSchema, min_length=1)


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]
