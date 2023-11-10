from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    location: str
    age: int

users_list = [
    User(name = 'Santiago', surname = 'Mejia Lopez', location = 'La Ceja', age = 23),
    User(name = 'Angie Sofia', surname = 'Lopez Capera', location = 'Medellin', age = 20),
    User(name = 'Carlos Andres', surname = 'Navarro Gil', location = 'La Ceja', age = 24)
]

# Metodos GET

@app.get('/')
async def root():
    return {'root_message': 'Bienvenido al root de FastAPI'}

@app.get('/users')
async def users():
    return users_list