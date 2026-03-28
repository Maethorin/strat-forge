"""Skill typing contracts for StratForge."""

import typing


@typing.runtime_checkable
class SkillDefinitionContract(typing.Protocol):
    """Describe the structural contract exposed by a skill definition entity."""

    name: str
    governing_attribute: object
    difficulty: object
    category: object
