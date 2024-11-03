import os
import joblib
import pandas as pd
import json
import logging


def init():
  global model
  model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'),'outputs', 'model.pkl')
  try:
    print("Loading model from path.")
    model = joblib.load(model_path)
    print("Loading successful.")
  except Exception as e:
    print(f"exception: {e}")
    raise
  
  assert model is not None, f"Model not loaded: {model}"

def run(raw_data_payload):
  data = pd.DataFrame(json.loads(raw_data_payload)["data"])
  predictions = model.predict(data)
  return predictions.tolist()