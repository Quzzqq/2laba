from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI(
    title = "Поиск на википедии"
)

@app.get('/language/pages/{word}')
def search(word: str, pages: int = 3, language: str = "en"):
    wikipedia.set_lang(language)
    return wikipedia.summary(word, sentences=pages),wikipedia.page(word).url

class Info(BaseModel):
    word: str
    pages: int = 3
    language: str = "en"

@app.post("/")
def Search(inf: Info):
    wikipedia.set_lang(inf.language)
    return wikipedia.summary(inf.word, sentences=inf.pages),wikipedia.page(inf.word).url