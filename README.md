# Helpdesk API (backend)

## Run it
pip install -r requirements.txt
uvicorn main:app --reload

## Test it
pytest

## Current status
- /health — working
- /predict — working with FAKE data (ML model not connected yet)
- routing.py — real logic, category -> team lookup