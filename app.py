from fastapi import FastAPI, Request
from kundali_calculator import generate_kundali
from chatbot import get_chatbot_response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/kundali/")
async def create_kundali(dob: str, time: str, place: str):
    kundali = generate_kundali(dob, time, place)
    return {"kundali": kundali}

@app.post("/chat/")
async def chatbot_query(query: str, kundali: dict):
    response = get_chatbot_response(query, kundali)
    return {"response": response}
