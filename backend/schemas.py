from pydantic import BaseModel
from typing import List

class StudyPlan(BaseModel):
    daily_plan: List[str]
    revision_strategy: List[str]
    exam_tips: List[str]
