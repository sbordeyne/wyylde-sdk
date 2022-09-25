from dataclasses import dataclass

from .user import UserResource


@dataclass
class CrushResource:
    id: int
    new: bool
    sender: UserResource
    ts: int
