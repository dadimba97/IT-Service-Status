from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "IT Service Status is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}