
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RepoPilot API",
    version="0.1.0"
)

# Allow the Vue development server to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RepoPilot API"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "RepoPilot Backend"
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RepoPilot API",
    version="0.1.0"
)

# Allow the Vue development server to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RepoPilot API"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "RepoPilot Backend"
    }
