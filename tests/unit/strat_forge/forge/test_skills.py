"""Unit tests for the ``strat_forge.forge.skills`` module."""

import strat_forge.forge.skills as skills


class TestGettingSkillsModuleDocumentation:
    """Describe the skills module documentation contract."""

    def test_should_define_the_skills_module_docstring(self) -> None:
        """Assert that the skills module exposes a top-level docstring."""
        assert skills.__doc__ == "Skill domain models for StratForge."


class TestCreatingSkillDefinition:
    """Describe the skill definition creation contract."""

    def test_should_create_a_skill_definition_from_domain_values(self) -> None:
        """Assert that a skill definition keeps the configured domain values."""
        skill_definition = skills.SkillDefinition.create(
            name="Broadsword",
            governing_attribute=skills.SkillAttribute.DEXTERITY,
            difficulty=skills.SkillDifficulty.AVERAGE,
            category=skills.SkillCategory.COMBAT,
        )

        assert skill_definition.name == "Broadsword"
        assert (
            skill_definition.governing_attribute
            is skills.SkillAttribute.DEXTERITY
        )
        assert skill_definition.difficulty is skills.SkillDifficulty.AVERAGE
        assert skill_definition.category is skills.SkillCategory.COMBAT

    def test_should_define_the_gurps_attribute_code_for_dexterity(self) -> None:
        """Assert that the dexterity skill attribute keeps its GURPS code."""
        assert skills.SkillAttribute.DEXTERITY.value == "DX"
