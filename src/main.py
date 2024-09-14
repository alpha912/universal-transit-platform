from fastapi import FastAPI

app = FastAPI(
    title="Universal Transit Platform API",
    description="An API to unify global public transportation data and services.",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
