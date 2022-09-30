from fastapi import FastAPI
from fastapi import Body

app = FastAPI()
db = {}


@app.get("/cart/{cart_id}")
def cart(cart_id: int):
    return db[cart_id]


@app.post("/cart/{cart_id}/product")
def create_cart(cart_id: str, body: dict = Body(...)):
    if cart_id not in db:
        db[cart_id] = {
            "id": cart_id,
            "lines": []
        }
    
    db[cart_id]["lines"].append(body)
    return db[cart_id]
