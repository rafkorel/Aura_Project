from fastapi import FastAPI

# Создаём приложение
app = FastAPI()

# Этот эндпоинт отвечает на главной странице
@app.get("/")
def root():
    return {"message": "Привет, мир! Это Aura Project"}

# Этот эндпоинт проверяет, жив ли сервер
@app.get("/health")
def health():
    return {"status": "healthy", "version": "0.0.1"}