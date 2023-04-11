from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
  "*"
]
app.add_middleware(
   CORSMiddleware,
   allow_origins = origins,
   allow_credentials = True,
   allow_methods = ["*"],
   allow_headers = ["*"]
)


data = []
class User(BaseModel):
    name: str
    email: str
    address: str

@app.post("/create")
def add_user(user: User):
    data.append(user.dict())
    return data

@app.get("/list")
def get_users():
   return data

@app.get("/user/{id}")
def get_user(id: int):
   id = id - 1
   return data[id]

@app.put("/user/{id}")
def update_user(id: int, user: User):
   data[id-1] = user
   return data

@app.delete("/user/{id}")
def delete_user(id: int):
   data.pop(id-1)
   return data