from pydantic import BaseModel, Field


class ClipModel(BaseModel):
    id: int          = Field(..., gt=0)
    player_name: str = Field(..., min_length=1, max_length=50)
    file_name: str   = Field(..., min_length=1, max_length=100)
    



