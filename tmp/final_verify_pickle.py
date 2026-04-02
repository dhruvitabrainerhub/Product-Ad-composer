import pickle
import os
from pathlib import Path

BASE_DIR = Path(r'c:\Users\Shrim\Desktop\Project product ad composer')
model_path = BASE_DIR / "notebooks" / "audience_predictor.pkl"

print(f"Testing model load from: {model_path}")
if model_path.exists():
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("SUCCESS: Pickle loaded the model correctly.")
        print(f"Model type: {type(model)}")
    except Exception as e:
        print(f"ERROR: Pickle failed to load the model. Reason: {e}")
else:
    print("ERROR: Model file not found.")
