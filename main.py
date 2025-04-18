from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Tradient backend is live!"}
