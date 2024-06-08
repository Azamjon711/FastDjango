from fastapi import FastAPI, security, HTTPException
from database import ENGINE, session

app = FastAPI()


@app.get("/")
async def landing():
    return {
        "message": "This is landing page"
    }

