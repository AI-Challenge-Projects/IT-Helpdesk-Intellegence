from fastapi import FastAPI
from pydantic import BaseModel
from routing import get_team
from model_services import load_model, predict_category
from priority import get_priority

app = FastAPI()
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
    return {
        "category": category,
        "priority": priority,          
        "confidence": round(confidence, 2),
        "routed_team": get_team(category)
    }


