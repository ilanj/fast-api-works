from typing import List

import spacy
from fastapi import FastAPI
from ml import nlp
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_main():
    return {"message" : "Hello world"}

@app.get("/extract/{id}")
def extract(article_id: int, q : str = None):
    nlp = spacy.load("en_core_web_sm")
    count = 0
    if q:
        doc = nlp(q)
        count = len(doc.ents)
    return {"id" : id, "q":q, "count" : count}

class Article(BaseModel):
    content: str
    comments: List[str] = []

@app.post("/analyze/")
def analyze(article:Article):
    doc = nlp(article.content)
    ents = []
    for ent in doc.ents:
        ents.append({"text":ent.text, "label": ent.label_})

    return {"msg": article.content, "comments": article.comments, "ents":ents}

@app.post("/analyze_list/")
def analyze_list(articles:List[Article]):
    ents = []
    comments = []
    for article in articles:
        for comment in article.comments:
            comments.append(comment.upper())
        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({"text":ent.text, "label": ent.label_})

    return {"ents":ents, "comments":comments}

