import json

notebook_path = r'c:\Users\Shrim\Desktop\Project product ad composer\notebooks\Personalized_Ad_Composer.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if 'joblib' in source and 'ml_pipeline' in source:
            print("Found target cell, performing migration...")
            new_source = source.replace('import joblib', 'import pickle')
            new_source = new_source.replace("MODEL_PATH = 'audience_predictor.joblib'", "MODEL_PATH = 'audience_predictor.pkl'")
            new_source = new_source.replace("joblib.dump(ml_pipeline, MODEL_PATH)", "with open(MODEL_PATH, 'wb') as f:\n    pickle.dump(ml_pipeline, f)")
            new_source = new_source.replace("Exporting model to .joblib file...", "Exporting model to .pkl file...")
            
            # Split back into lines
            cell['source'] = [line + '\n' for line in new_source.split('\n')]
            # Remove trailing newline from last line if it didn't have one originally
            if cell['source'][-1] == '\n':
                cell['source'].pop()

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook migration complete.")
