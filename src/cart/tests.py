from fastapi.testclient import TestClient
from src.cart.views import app, db

client = TestClient(app)


# TEST RETURN CART BY ID
def test_return_cart():
    db["1"] = {
        "id": "1",
        "lines": [
            {"product": 50776},
            {"product": 15778}
        ]
    }

    response = client.get("/cart/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": "1",
        "lines": [
            {"product": 50776},
            {"product": 15778}
        ]
    }

# TEST ADD PRODUCT TO THE CART
def test_add_product_to_cart():
    db["1"] = {
        "id": "1",
        "lines": [
            {"product": 15778}
        ]
    }
    body = {"product": 50776}
    
    response = client.post("/cart/1/product", json=body)
    
    assert response.status_code == 200
    assert response.json() == {
        "id": "1",
        "lines": [
            {"product": 15778},
            {"product": 50776},
        ]
    }


# TEST SUM QUANTITY TO A PRODUCT OF THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST SUBSTRACT PRODUCT OF THE CART
def test_delete_product_of_cart():
    db["1"] = {
        "id": "1",
        "lines": [
            {"product": 50776}
        ]
    }
    body = {"product": 50776}
    
    response = client.delete("/cart/1/product", json=body)

    assert response.status_code == 200
    assert response.json() == {
        "id": "1",
        "lines": []
    }


# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST REST QUANTITY OF A PRODUCT OF THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST CANT REST MORE QUANTITY THAN EXISTS OF A PRODUCT OF THE CART
def test_can_not_rest_more_than_5():
    db["1"] = {
        "id": "1",
        "lines": [
            {"product": 50776},
            {"product": 50776},
            {"product": 50776},
            {"product": 50776},
            {"product": 50776},
            {"product": 50776},
        ]
    }
    body = {"product": 50776, "quantity": 6}
    
    response = client.delete("/cart/1/product", json=body)

    assert response.status_code == 400
    assert response.json() == {
        "error": "Nooooo primo nooo",
    }

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST CLEAR THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST ADD TOTAL TO THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?