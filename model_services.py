import joblib
import os

model = None
vectorizer = None

def load_model():
    global model, vectorizer
    if os.path.exists("ml_artifacts/category_model.pkl"):
        model = joblib.load("ml_artifacts/category_model.pkl")
        vectorizer = joblib.load("ml_artifacts/tfidf_vectorizer.pkl")
        print("Real model loaded.")
    else:
        print("No model found yet — using fake predictions.")

def predict_category(ticket_text: str) -> tuple[str, float]:
    if model is None or vectorizer is None:
        return "Hardware", 0.87
    X = vectorizer.transform([ticket_text])
    prediction = model.predict(X)[0]
    confidence = max(model.predict_proba(X)[0])
    return prediction, float(confidence)

def get_model_status() -> dict:
    return {
        "model_loaded": model is not None,
        "mode": "real" if model is not None else "fake"
    }

