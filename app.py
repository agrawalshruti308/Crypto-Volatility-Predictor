import os
import sys
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

# This adds the absolute path of your project to Python's brain
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

try:
    # We are using 'crypto' directly because pip install -e . and sys.path make it visible
    from crypto.pipeline.training_pipeline import TrainPipeline
    from crypto.pipeline.prediction_pipeline import PredictionPipeline, CryptoData
    from logger import logging
    from exception import CustomException
    print("SUCCESS: Modules loaded!")
except Exception as e:
    print(f"STILL AN ERROR: {e}")

app = FastAPI()

@app.get("/")
async def index():
    return {"status": "Ready"}

# ... (rest of your routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)