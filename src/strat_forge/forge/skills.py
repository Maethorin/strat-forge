"""Skill domain models for StratForge."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Self


class SkillAttribute(StrEnum):
    """Represent the governing attribute of a GURPS skill."""

    STRENGTH = "ST"
    DEXTERITY = "DX"
    INTELLIGENCE = "IQ"
    HEALTH = "HT"
    WILL = "Will"
    PERCEPTION = "Per"

    @classmethod
    def create(cls, value: str) -> Self:
        """Create a skill attribute from its canonical GURPS code."""
        return cls(value)


class SkillDifficulty(StrEnum):
    """Represent the difficulty progression of a GURPS skill."""

    EASY = "E"
    AVERAGE = "A"
    HARD = "H"
    VERY_HARD = "VH"

    @classmethod
    def create(cls, value: str) -> Self:
        """Create a skill difficulty from its canonical GURPS code."""
        return cls(value)


class SkillCategory(StrEnum):
    """Classify a skill by its functional family inside the engine."""

    COMBAT = "combat"
    SOCIAL = "social"
    TECHNICAL = "technical"
    MOVEMENT = "movement"
    WILDERNESS = "wilderness"
    SCHOLARLY = "scholarly"

    @classmethod
    def create(cls, value: str) -> Self:
        """Create a skill category from its canonical category name."""
        return cls(value)


@dataclass(frozen=True, slots=True)
class SkillDefinition:
    """Describe the immutable domain definition of a skill."""

    name: str
    governing_attribute: SkillAttribute
    difficulty: SkillDifficulty
    category: SkillCategory

    @classmethod
    def create(cls, name: str, governing_attribute: SkillAttribute, difficulty: SkillDifficulty, category: SkillCategory) -> Self:
        """Create a skill definition from its core domain values."""
        return cls(name=name, governing_attribute=governing_attribute, difficulty=difficulty, category=category)
