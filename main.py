from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'root_message': 'Bienvenido al root de FastAPI'}