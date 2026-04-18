# agent/tools.py

from db.database import SessionLocal
from db.models import Interaction
from datetime import datetime


# ---------------- LOG INTERACTION ----------------
def log_interaction_tool(data: str):
    db = SessionLocal()

    try:
        # 🔍 Extract doctor name
        match = re.search(r"Dr\.?\s+[A-Za-z]+", data)
        hcp_name = match.group(0) if match else "Unknown"

        # 😊 Simple sentiment detection
        sentiment = "positive" if "positive" in data.lower() else "neutral"

        interaction = Interaction(
            hcp_name=hcp_name,
            hcp_id=None,
            message=data,
            sentiment=sentiment,
            created_at=datetime.utcnow()
        )

        db.add(interaction)
        db.commit()

        return f"Stored: {hcp_name} | {sentiment}"

    except Exception as e:
        db.rollback()
        return str(e)

    finally:
        db.close()

# ---------------- EDIT INTERACTION ----------------
def edit_interaction_tool(data: str):
    return f"Edited interaction: {data}"


# ---------------- FETCH HISTORY ----------------
def fetch_history_tool(user_id: str = "default_user"):
    db = SessionLocal()

    try:
        records = db.query(Interaction).all()

        return [
            {
                "id": r.id,
                "hcp_name": r.hcp_name,
                "message": r.message,
                "sentiment": r.sentiment,
                "created_at": str(r.created_at)
            }
            for r in records
        ]

    except Exception as e:
        return f"DB Error: {str(e)}"

    finally:
        db.close()


# ---------------- FOLLOW UP ----------------
def follow_up_suggestion_tool(context: str):
    return f"Follow-up suggestion for: {context}"