from fastapi import FastAPI
from pydantic import BaseModel
from routing import get_team

app = FastAPI()

class TicketRequest(BaseModel):
    ticket_text: str

@app.get("/health")
def health():
    return {"message": "ok"}

@app.post("/predict")
def predict(ticket: TicketRequest):
    fake_category = "Hardware"
    return {
        "category": fake_category,
        "priority": "High",
        "confidence": 0.87,
        "routed_team": get_team(fake_category)
    }

