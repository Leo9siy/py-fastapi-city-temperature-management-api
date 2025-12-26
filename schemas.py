from typing import List

from pydantic import BaseModel


class CitySchema(BaseModel):
    name: str
    additional_info: str


class CityResponseSchema(CitySchema):
    id: int


class CityListSchema(BaseModel):
    cities: List[CityResponseSchema]

    model_config = {"from_attributes": True}


