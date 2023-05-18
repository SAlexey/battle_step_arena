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
        """
        Check if the character is alive
        """
        return self.health > 0

    @property
    def melee_attack(self) -> int:
        """
        Calculate the melee attack points
        """
        return self.strength + self.intelligence

    @property
    def ranged_attack(self) -> int:
        """
        Calculate the ranged attack points
        """
        return self.dexterity + self.intelligence

    @property
    def special_attack(self) -> int:
        """
        Calculate the special attack points
        """
        return self.strength + self.intelligence + self.dexterity

    @property
    def max_experience(self) -> int:
        """
        Calculate the max experience points
        """
        return self.level * 100 + 1
