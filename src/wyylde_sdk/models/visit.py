from dataclasses import dataclass

from .user import UserResource


@dataclass
class VisitResource:
    id: int
    new: bool
    sender: UserResource
    ts: int
