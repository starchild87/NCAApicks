import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

application = app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process", response_class=HTMLResponse)
async def process(request: Request,
                  lines: str = Form(...)):
    print(lines)
    print(len(lines))
    items = lines.split("\t")
    print(len(items))
    num = ''
    ndx = 0
    for item in items:
        if ndx % 3 == 0:
            for c in item:
                if c.isdigit():
                    num += str(c)
            print(num)
            num = ''
        ndx += 1
    return templates.TemplateResponse("index.html", {"request": request, "lines": lines})