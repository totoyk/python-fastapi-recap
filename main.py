from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cat/{cat_id}")
def read_item(cat_id: int, q: str = None):
    if q is None:
      q = "Meow"
    return {"cat_id": cat_id, "q": q}
