# IT Helpdesk Intelligence System

This is an ML-powered IT Helpdesk routing system. The frontend is a static HTML file that communicates with a Python/FastAPI backend to predict ticket categories, priorities, routed teams, and estimated resolution times.

## 🚀 How to Run the Project Locally

Because the frontend relies on the machine learning models to make predictions, **you must start the Python backend first** before interacting with the HTML file.

### 1. Set up the Backend
Open a terminal in the project folder and run the following commands to set up your environment and start the server:

**For Windows:**
`powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
`

**For Mac/Linux:**
`ash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
`

### 2. Open the Frontend
Once the terminal says Application startup complete, the API is running locally at http://127.0.0.1:8000. 

Now, simply double-click the **index.html** file in the root folder to open it in your default web browser. Type a ticket into the system (e.g., *"my laptop won't turn on"*) and click **Predict**!

## 🏗️ Architecture
* **Frontend:** Vanilla HTML/JS/CSS (index.html). Sends the ticket text via a etch() POST request to the backend.
* **Backend:** Python FastAPI (main.py). Receives the request and handles routing logic.
* **Machine Learning:** Scikit-Learn (model_services.py). Loads category_model.pkl and 	fidf_vectorizer.pkl via joblib to predict the issue category.
