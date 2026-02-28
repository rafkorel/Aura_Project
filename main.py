from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users_db = []

class NameRequest(BaseModel):
    name: str

@app.get("/")
def root():
    return {"message": "Привет, мир! Это Aura Project"}

@app.get("/health")
def health():
    return {"status": "healthy", "version": "0.0.1"}

@app.post("/hello")
def say_hello(request: NameRequest):
    users_db.append(request.name)
    return {"message": f"Привет, {request.name}!", "all_users": users_db}

@app.get("/users")
def get_users():
    return {"users": users_db}