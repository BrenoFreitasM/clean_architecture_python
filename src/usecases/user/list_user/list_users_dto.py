from pydantic import BaseModel
from domain.user.user_entity import user
from typing import List
from uuid import UUID

# INPUT

class ListUsersInputDto(BaseModel):
    pass

# DTO INTERMEDIÁRIO
class UserDto(BaseModel):
    id: UUID
    name: str

# OUTPU
class ListUsersOutputDto(BaseModel):
    users: List[UserDto]

# user_dto = UserDto(id=1, name="Alexandre") #ERROR
# user_dto = UserDto(id=uuid4(), name="Mariana") # Não vai dar erro (BaseModel vai validar)