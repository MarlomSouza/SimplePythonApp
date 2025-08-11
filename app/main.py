from fastapi import FastAPI
from datetime import datetime, timezone
import os

app = FastAPI(title="SimplePythonApp")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/env")
def get_env():
    # Convert os.environ (mapping) to a regular dict (values as strings)
    return {k: v for k, v in os.environ.items()}


@app.get("/time")
def get_time():
    now = datetime.now(timezone.utc).isoformat()
    return {"utc_time": now}


def create_app() -> FastAPI:
    return app
