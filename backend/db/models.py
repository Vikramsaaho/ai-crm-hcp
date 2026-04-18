from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from db.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255), nullable=False)
    hcp_id = Column(String(100))

    message = Column(Text, nullable=False)
    sentiment = Column(String(50))

    created_at = Column(DateTime, default=datetime.utcnow)


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    hcp_id = Column(String(100), unique=True)

    specialty = Column(String(100))
    hospital = Column(String(255))
    region = Column(String(100))

    created_at = Column(DateTime, default=datetime.utcnow)