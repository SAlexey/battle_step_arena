from dataclasses import dataclass, field
from typing import Optional, List

# from item.base import Item
# from item.weapon import Weapon
# from item.armor import Armor


@dataclass
class Character:
    name: str = field(repr=True)
    type: str = field(repr=True)
    health: int = field(repr=False, default=0)
    max_health: int = field(repr=False, default=100)
    level: int = field(repr=True, default=1)
    experience: int = field(repr=False, default=0)
    strength: int = field(repr=False, default=1)
    intelligence: int = field(repr=False, default=1)
    dexterity: int = field(repr=False, default=1)
    # weapons: List[Weapon] = field(repr=False, default_factory=list)
    # items: List[Item] = field(repr=False, default_factory=list)
    # armor: List[Armor] = field(repr=False, default_factory=list)

    def __post_init__(self) -> None:
        self.health = self.max_health

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    @property
    def melee_attack(self) -> int:
        return self.strength + self.dexterity

    @property
    def ranged_attack(self) -> int:
        return self.dexterity + self.intelligence

    @property
    def special_attack(self) -> int:
        return self.strength + self.intelligence + self.dexterity

    @property
    def max_experience(self) -> int:
        return self.level * 100 + 1
