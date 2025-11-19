import joblib

# Save preprocessor
preprocessor = joblib.load(".\models\preprocessor.pkl")

# Save Ridge model
model = joblib.load(".\models\Ridge_model.pkl")
