from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

class ScenarioOptionsSchema(BaseModel):
    text:str
    node_id:Optional[int] = None


class ScenarioNodeBase(BaseModel):
    content:str
    is_ending: bool = False
    is_winning_ending:bool = False


class CompleteScenarioNodeResponse(ScenarioNodeBase):
    id: int
    options: List[ScenarioOptionsSchema] = []

    class Config:
        from_attributes = True


class ScenarioBase(BaseModel):
    title:str
    session_id: Optional[str] = None

    class Config:
        from_attributes = True



class CreateScenarioRequest(BaseModel):
    theme:str


class CompleteScenarioResponse(ScenarioBase):
    id: int
    created_at: datetime
    root_node: CompleteScenarioNodeResponse
    all_nodes:Dict[int, CompleteScenarioNodeResponse]

    class Config:
        from_attributes = True