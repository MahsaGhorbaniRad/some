from fastapi import FastAPI

app = FastAPI()

@app.get("/home")

def string():
    return "hello world"

