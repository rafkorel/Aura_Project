from fastapi import FastAPI
from pydantic import BaseModel  # <-- Добавь эту строчку вверху

app = FastAPI()

# Добавь эту модель (класс) где-нибудь перед функцией
class NameRequest(BaseModel):
    name: str

@app.get("/")
def root():
    return {"message": "Привет, мир! Это Aura Project"}

@app.get("/health")
def health():
    return {"status": "healthy", "version": "0.0.1"}

@app.post("/hello")
def say_hello(request: NameRequest):  # <-- Изменённая строка
    return {"message": f"Привет, {request.name}!"}