from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/{id}")
async def root(id:int):
    return {"id": id}