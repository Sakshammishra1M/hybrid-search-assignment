from fastapi import FastAPI
from pydantic import BaseModel
from backend.app.search_engine import SearchEngine

app = FastAPI()

engine = SearchEngine()


class SearchRequest(BaseModel):

    query: str
    top_k: int = 10
    alpha: float = 0.5


@app.get("/health")
def health():

    return {"status": "ok"}


@app.post("/search")
def search(req: SearchRequest):

    results = engine.search(req.query, req.top_k, req.alpha)

    return {
        "query": req.query,
        "results": results
    }