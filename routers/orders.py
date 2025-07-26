# routers/orders.py
from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel, Field
import time

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

class OrderCreate(BaseModel):
    customer_name: str = Field(..., min_length=1)
    items: list[str] = Field(..., min_items=1)
    address: str = Field(..., min_length=5)

def notify_staff(order: dict):
    # Simulate a slow notification (like sending an email or message)
    print(f"[Notify] New order received: {order}")
    time.sleep(2)  # Simulate delay (do NOT do this in real async functions)
    print(f"[Notify] Staff notified for order from {order['customer_name']}")

@router.post("/", status_code=201)
async def place_order(order: OrderCreate, background_tasks: BackgroundTasks):
    # Here, you'd create the order, e.g., save to a DB
    order_data = order.dict()
    print(f"[Order] Creating order: {order_data}")
    # Offload staff notification to background
    background_tasks.add_task(notify_staff, order_data)
    return {"message": "Order placed successfully!"}
