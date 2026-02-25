from typing import List
from pydantic import BaseModel


class SortRequest(BaseModel):
    numbers: List[int]


class SortResponse(BaseModel):
    sorted_numbers: List[int]
