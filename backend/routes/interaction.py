from fastapi import APIRouter
from db.database import SessionLocal
from db.models import Interaction

router = APIRouter()

@router.get("/history")
def get_history():
    db = SessionLocal()
    interactions = db.query(Interaction).all()

    result = []
    for i in interactions:
        result.append({
            "hcp_name": i.hcp_name,
            "message": i.message,
            "sentiment": i.sentiment
        })

    db.close()
    return result