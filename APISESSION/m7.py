from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Campus Cafe")

orders = {1: {"student": "Asha", "item": "Cold coffee", "qty": 2,
              "price": 60.5, "extras": ["ice"], "paid": False}}

class Order(BaseModel):          # validates the incoming JSON
    student: str
    item: str
    qty: int
    price: float
    extras: list[str] = []
    paid: bool = False

@app.get("/orders")
def all_orders():
    return orders

@app.get("/orders/{oid}")
def one_order(oid: int):
    if oid not in orders:
        raise HTTPException(404, "Order not found")
    return orders[oid]

@app.post("/orders", status_code=201)
def new_order(o: Order):
    oid = max(orders, default=0) + 1
    orders[oid] = o.model_dump()
    return {"id": oid, **orders[oid]}

@app.put("/orders/{oid}")
def replace_order(oid: int, o: Order):
    if oid not in orders:
        raise HTTPException(404, "Order not found")
    orders[oid] = o.model_dump()
    return orders[oid]

@app.delete("/orders/{oid}")
def cancel_order(oid: int):
    if orders.pop(oid, None) is None:
        raise HTTPException(404, "Order not found")
    return {"cancelled": oid}
