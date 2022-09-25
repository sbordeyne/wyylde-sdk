from dataclasses import dataclass

from .user import UserResource


@dataclass
class CrushResource:
    id: str
    new: bool
    sender: UserResource
    ts: int
