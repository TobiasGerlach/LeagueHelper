from typing import List
from attr import dataclass


@dataclass
class Item:
    _COOLDOWNS: List[int]
    _STATIC_COOLDOWN: int
    _MAGIC_DMG: List[int]
    _PHYSICAL_DMG: List[int]
    _ABSOLUTE_DMG: List[int]
    _HEAL: List[int]
    _cooldown: float = None
