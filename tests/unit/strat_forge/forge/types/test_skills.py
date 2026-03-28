"""Unit tests for the ``strat_forge.forge.types.skills`` module."""

from strat_forge.forge.entities import skills as entity_skills
from strat_forge.forge.types import skills


class TestGettingSkillTypesModuleDocumentation:
    """Describe the skill types module documentation contract."""

    def test_should_define_the_skill_types_module_docstring(self) -> None:
        """Assert that the skill types module exposes a top-level docstring."""
        assert skills.__doc__ == "Skill typing contracts for StratForge."


class TestMatchingSkillProtocols:
    """Describe the skill protocol conformance contract."""

    def test_should_match_the_skill_definition_protocol(self) -> None:
        """Assert that the concrete skill definition entity conforms to the skill protocol."""
        skill_definition = entity_skills.SkillDefinition.create(name="Broadsword", governing_attribute=entity_skills.SkillAttribute.DEXTERITY, difficulty=entity_skills.SkillDifficulty.AVERAGE, category=entity_skills.SkillCategory.COMBAT)

        assert isinstance(skill_definition, skills.SkillDefinitionContract)
