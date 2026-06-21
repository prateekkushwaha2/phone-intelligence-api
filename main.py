from fastapi import FastAPI
from routes.phone import router

app = FastAPI(
  title="phone Intelligence API",
  version="1.0"
)  

app.include_router(router)

@app.get("/")
def home():
  return {
    "message": "Phone Intelligence API Running"
  }
  
