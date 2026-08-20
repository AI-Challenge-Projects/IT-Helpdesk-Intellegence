import os
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from routing import get_team
from model_services import load_model, predict_category
from priority import get_priority
from fastapi.middleware.cors import CORSMiddleware
from resolution_time import estimate_resolution_hours
from model_services import load_model, predict_category, get_model_status
from dotenv import load_dotenv

load_model()
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Helpdesk API"))
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TicketRequest(BaseModel):
    ticket_text: str

@app.get("/health")
def health():
    return {"message": "ok"}

@app.post("/predict")
def predict(ticket: TicketRequest):
    logger.info(f"Received ticket: {ticket.ticket_text[:50]}...")
    category, confidence = predict_category(ticket.ticket_text)
    priority = get_priority(ticket.ticket_text)
    estimated_hours = estimate_resolution_hours(category, priority)
    logger.info(f"Predicted: category={category}, priority={priority}, confidence={confidence}")
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

