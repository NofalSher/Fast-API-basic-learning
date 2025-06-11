from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}   


@app.get("/about")
async def about() -> str:
    return "Learn FastAPI for building ML APIs"