import pickle
import os

model = None
vectorizer = None

def load_model():
    global model, vectorizer
    if os.path.exists("ml_artifacts/model.pkl"):
        with open("ml_artifacts/model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("ml_artifacts/vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        print("Real model loaded.")
    else:
        print("No model found yet — using fake predictions.")

def predict_category(ticket_text: str) -> tuple[str, float]:
    if model is None or vectorizer is None:
        # FAKE fallback — used until ML hands off real files
        return "Hardware", 0.87
    X = vectorizer.transform([ticket_text])
    prediction = model.predict(X)[0]
    confidence = max(model.predict_proba(X)[0])
    return prediction, float(confidence)