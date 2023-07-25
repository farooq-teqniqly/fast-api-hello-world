from datetime import datetime
from uuid import UUID
from starlette.responses import Response
from starlette import status
from orders.app import app
from orders.models import CreateOrderSchema

orders = {
    "3d82eea9-7498-430f-9344-7fca4580fa62": {
        "id": "3d82eea9-7498-430f-9344-7fca4580fa62",
        "status": "delivered",
        "created": datetime.utcnow(),
        "items": {
            "product": "cappuccino",
            "size": "medium",
            "quantity": 1
        }
    },
    "553ed79e-0542-46e6-9761-41fc1eed6005": {
        "id": "3d82eea9-7498-430f-9344-7fca4580fa62",
        "status": "delivered",
        "created": datetime.utcnow(),
        "items": {
            "product": "cappuccino",
            "size": "medium",
            "quantity": 1
        }
    }
}


@app.get("/orders", status_code=status.HTTP_200_OK)
def get_orders():
    return {"orders": orders}


@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order():
    return orders["3d82eea9-7498-430f-9344-7fca4580fa62"]


@app.put("/orders/{order_id}", status_code=status.HTTP_200_OK)
def update_order(order_id: UUID):
    order = orders.get(str(order_id))

    if order is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return order


@app.get("/orders/[order_id]", status_code=status.HTTP_200_OK)
def get_order(order_id: UUID):
    order = orders.get(str(order_id))

    if order is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return order
