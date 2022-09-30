from fastapi import FastAPI
from fastapi import Body
from fastapi.responses import JSONResponse

app = FastAPI()
db = {}


@app.get("/cart/{cart_id}")
def cart(cart_id: str):
    return db[cart_id]


@app.post("/cart/{cart_id}/product")
def create_cart(cart_id: str, body: dict = Body(...)):
    db[cart_id]["lines"].append(body)
    return db[cart_id]

@app.delete("/cart/{cart_id}/product")
def delete_cart(cart_id: str, body: dict = Body(...)):
    LIMIT = 5
    
    if "quantity" in body and body["quantity"] > LIMIT:
        return JSONResponse(status_code=400, content={"error": "Nooooo primo nooo"})
    
    db[cart_id]["lines"].remove(body)
    return db[cart_id]
