from character.base import Character
import pytest


@pytest.fixture()
def character():
    character = Character(
        name="name",
        type="type",
        health=100,
        max_health=100,
    )
    return character


def test_character_health_at_init_is_equal_to_max_health_at_init(character):
    assert character.health == character.max_health


def test_character_experience_is_zero_at_init(character):
    assert character.experience == 0


def test_character_melee_attack_is_sum_of_strength_and_dexterity(character):
    assert character.melee_attack == character.strength + character.dexterity


def test_character_ranged_attack_is_sum_of_dexterity_and_intelligence(character):
    assert character.ranged_attack == character.dexterity + character.intelligence


def test_character_is_alive_when_health_is_at_max_health(character):
    character.health = character.max_health
    assert character.is_alive


def test_character_is_alive_when_health_is_below_zero(character):
    character.health = -1
    assert not character.is_alive


def test_character_is_alive_when_health_is_above_zero(character):
    character.health = 1
    assert character.is_alive


def test_character_is_alive_when_health_is_zero(character):
    character.health = 0
    assert not character.is_alive
