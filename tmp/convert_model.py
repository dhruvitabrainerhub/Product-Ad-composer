import joblib
import pickle
import os

model_path = r'c:\Users\Shrim\Desktop\Project product ad composer\notebooks\audience_predictor.pkl'

if os.path.exists(model_path):
    print(f"Loading existing model from {model_path} using joblib...")
    try:
        # Load with joblib
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        
        # Save with pickle
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        print(f"Model re-saved successfully to {model_path} using pickle format.")
        
        # Verify
        with open(model_path, 'rb') as f:
            verified_model = pickle.load(f)
        print("Verification successful: Model can be read by pickle.")
        
    except Exception as e:
        print(f"Error during conversion: {e}")
else:
    print(f"Model not found at {model_path}")
