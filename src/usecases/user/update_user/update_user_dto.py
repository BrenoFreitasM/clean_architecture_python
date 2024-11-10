from pydantic import BaseModel
from uuid import UUID

# INPUT

class updateUserInputDto(Basemodel):
    id: UUID

# OUTPUT
class updateUserOutputDto(BaseModel):
    id: UUID
    name: str