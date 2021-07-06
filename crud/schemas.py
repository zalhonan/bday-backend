from pydantic import BaseModel
from typing import Text, Union, Optional

from pydantic.types import Json


class Events(BaseModel):
    # * базовая модель группы событий. В events будет json событий
    token: str
    language: str
    timezone: int
    events: str

    class Config:
        orm_mode = True
