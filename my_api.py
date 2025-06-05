# api_server.py - Il tuo server API standalone
from fastapi import FastAPI
from typing import List
import uvicorn

app = FastAPI(title="My API Server")

# Storage semplice
notes = []
counter = 0

@app.post("/add_note")
async def add_note(text: str) -> dict:
    """Aggiunge una nota"""
    global counter
    counter += 1
    note = {"id": counter, "text": text}
    notes.append(note)
    return {"success": True, "note": note}

@app.get("/list_notes")
async def list_notes() -> List[dict]:
    """Lista tutte le note"""
    return notes

@app.post("/calculate")
async def calculate(a: float, b: float, operation: str = "add") -> dict:
    """Fa calcoli semplici"""
    ops = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero"
    }
    result = ops.get(operation, "Unknown operation")
    return {"a": a, "b": b, "operation": operation, "result": result}

if __name__ == "__main__":
    # Avvia il server API su porta 8000
    print("🌐 Starting API server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)