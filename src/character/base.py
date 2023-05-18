from dataclasses import dataclass, field


@dataclass
class Character:
    """
    Base character class
    """

    name: str = field(repr=True)
    type: str = field(repr=True)
    health: int = field(repr=False, default=0)
    max_health: int = field(repr=False, default=100)
    level: int = field(repr=True, default=1)
    experience: int = field(repr=False, default=0)
    strength: int = field(repr=False, default=1)
    intelligence: int = field(repr=False, default=1)
    dexterity: int = field(repr=False, default=1)

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
