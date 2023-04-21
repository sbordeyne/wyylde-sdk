from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, Union


class ProfileType(IntEnum):
    COUPLE_HETERO = 3
    COUPLE_FBI = 4
    COUPLE_HBI = 5
    COUPLE_BI = 6
    WOMAN_HETERO = 2
    WOMAN_BI = 9
    WOMAN_HOMO = 10
    MAN_HETERO = 1
    MAN_BI = 7
    MAN_HOMO = 8
    TRAV = 12
    TRANS = 13


@dataclass
class UserResource:
    id: int
    nickname: Optional[str] = ''
    blacklisted: Optional[bool] = False
    deleted: Optional[bool] = False
    blocked: Optional[bool] = False
    online: Optional[Union[str, bool]] = False
    url_id: Optional[str] = None
    profile_type: Optional[ProfileType] = None
    certified: Optional[bool] = None
    tonight: Optional[bool] = None
    week_availability: Optional[bool] = None
    device: Optional[str] = None
    filtered: Optional[bool] = None
    language: Optional[str] = None
    geo_code3: Optional[str] = None
    geoposition: Optional[str] = None
    postal_address: Optional[str] = None
    main_pic: Optional[str] = None
    p0_age: Optional[int] = None
    p0_gender: Optional[str] = None
    p1_age: Optional[int] = None
    p1_gender: Optional[str] = None

    @property
    def is_couple(self) -> bool:
       return self.profile_type in (
        ProfileType.COUPLE_BI, ProfileType.COUPLE_FBI,
        ProfileType.COUPLE_HBI, ProfileType.COUPLE_HETERO,
    )

    @property
    def is_lady(self) -> bool:
        return self.profile_type in (
            ProfileType.WOMAN_HOMO, ProfileType.WOMAN_BI,
            ProfileType.WOMAN_HETERO,
        )

    @property
    def is_man(self) -> bool:
        return self.profile_type in (
            ProfileType.MAN_HOMO, ProfileType.MAN_BI,
            ProfileType.MAN_HETERO,
        )

    @property
    def is_trav(self) -> bool:
        return self.profile_type == ProfileType.TRAV

    @property
    def is_trans(self) -> bool:
        return self.profile_type == ProfileType.TRANS
