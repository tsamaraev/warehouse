from fastapi import FastAPI
from routes import rolls

app = FastAPI()

app.include_router(rolls.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
