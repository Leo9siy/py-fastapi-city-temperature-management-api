from datetime import datetime
from typing import List

from pydantic import BaseModel


class TempSchema(BaseModel):
    city_id: int | None
    date_time: datetime | None
    temperature: float | None

    model_config = {"from_attributes": True}


class TempListSchema(BaseModel):
    temps: List[TempSchema]
