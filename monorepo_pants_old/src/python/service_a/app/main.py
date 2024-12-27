from fastapi import FastAPI
import uvicorn

from shared_model.product import ProductResponse




app = FastAPI()

# Sample product data
products_data = [
    {"id": 1, "name": "Product 1", "description": "Description 1", "price": 19.99},
    {"id": 2, "name": "Product 2", "description": "Description 2", "price": 29.99},
]

@app.get("/get_all_products", response_model=list[ProductResponse])
async def get_all_products():
    # Return all products
    return products_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)