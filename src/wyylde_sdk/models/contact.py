from dataclasses import dataclass
from typing import Optional

from .user import UserResource


@dataclass
class ContactUserResource:
    card: UserResource
    comment: str
    email: str
    mobile: str
    phone: str
    url_id: str
