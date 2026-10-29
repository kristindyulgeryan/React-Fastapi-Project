import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie,Response,BackgroundTasks
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.scenario import Scenario, ScenarioNode
from backend.models.job import ScenarioJob
from backend.schemas.scenario import (
    CompleteScenarioResponse, CompleteScenarioNodeResponse, CreateScenarioRequest
)
from backend.schemas.job import ScenarioJobResponse

router = APIRouter(
    prefix="/scenarios"
    tags=["scenarios"]
)

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id
