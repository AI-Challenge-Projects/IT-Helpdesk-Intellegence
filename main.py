from fastapi import FastAPI
from pydantic import BaseModel
from routing import get_team
from model_services import load_model, predict_category
from priority import get_priority
from fastapi.middleware.cors import CORSMiddleware
from resolution_time import estimate_resolution_hours
from model_services import load_model, predict_category, get_model_status

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

load_model()

class TicketRequest(BaseModel):
    ticket_text: str

@app.get("/health")
def health():
    return {"message": "ok"}

@app.post("/predict")
def predict(ticket: TicketRequest):
    category, confidence = predict_category(ticket.ticket_text)
    priority = get_priority(ticket.ticket_text)
    estimated_hours = estimate_resolution_hours(category, priority)
    return {
        "category": category,
        "priority": priority,
        "confidence": round(confidence, 2),
        "routed_team": get_team(category),
        "estimated_resolution_hours": estimated_hours
    }

@app.get("/model")
def model_status():
    return get_model_status()
