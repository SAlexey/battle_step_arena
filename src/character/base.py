from dataclasses import dataclass, field


@dataclass
class Character:
    """
    Base character class
    """

    # the character's name
    name: str = field(repr=True)
    # the character's type
    type: str = field(repr=True)
    # the character's health
    health: int = field(repr=False, default=0)
    # the character's maximum health
    max_health: int = field(repr=False, default=100)
    # the character's level
    level: int = field(repr=True, default=1)
    # the character's experience
    experience: int = field(repr=False, default=0)
    # the character's strength
    strength: int = field(repr=False, default=1)
    # the character's intelligence
    intelligence: int = field(repr=False, default=1)
    # the character's dexterity
    dexterity: int = field(repr=False, default=1)

    def __post_init__(self) -> None:
        # at initialization, set the character's health to the maximum
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
