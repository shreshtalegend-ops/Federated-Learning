from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Federated Aggregation Server")

class WeightPayload(BaseModel):
    client_id: str
    round_number: int
    weights: Dict[str, Any]

@app.get("/")
async def root():
    return {"message": "Welcome to the Federated Aggregation Server"}

@app.get("/health")
async def health_check():
    """Basic health check to ensure the server is responsive."""
    return {"status": "ok", "message": "Aggregation server is running."}

@app.post("/upload-weights")
async def upload_weights(payload: WeightPayload):
    """
    Placeholder endpoint to receive local model weights.
    In Phase 3, this will route data to the FedAvg logic.
    """
    return {
        "status": "success",
        "client": payload.client_id,
        "message": f"Weights received for round {payload.round_number}"
    }