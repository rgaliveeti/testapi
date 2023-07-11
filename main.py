from fastapi import FastAPI


app = FastAPI()


data = {"data":
  [{
    "category": "men's clothing",
    "description":
      "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "id": 1,
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    "price": 109.95,
    "Size": [
      { "size": 9, "sku": 1 },
      { "size": 9, "sku": 2 },
    ],
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
  },
  {
    "category": "men's clothing",
    "description":
      "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "id": 1,
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    "price": 129.95,
    "Size": [
      { "size": 8, "sku": 1 },
      { "size": 9, "sku": 2 },
    ],
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
  },
  {
    "category": "men's clothing",
    "description":
      "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    id: 2,
    "image":
      "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
    "price": 22.3,
    "Size": [
      { "size": 8, "sku": 1 },
      { "size": 9, "sku": 2 },
    ],
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
  }]
       }

@app.get("/")
async def index():
    return data
