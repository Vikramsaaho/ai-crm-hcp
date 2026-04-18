from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine
from db.models import Base

from routes.interaction import router as interaction_router
from routes.ai_chat import router as ai_chat_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-First CRM (HCP Module)",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(interaction_router, prefix="/api")
app.include_router(ai_chat_router, prefix="/api")


@app.get("/")
def home():
    return {"message": "AI CRM Backend Running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}