from pydantic import BaseModel


class LaunchRequest(BaseModel):
    provider: str
    rocket: str
    mission_type: str
    pad: str

    year: int
    month: int
    day: int
    hour: int