"""Unit tests for the project pyproject configuration."""

from pathlib import Path
import tomllib


class TestGettingPyprojectOptionalDependencies:
    """Describe the optional dependency configuration."""

    def test_should_include_ruff_in_the_dev_dependencies(self) -> None:
        """Assert that Ruff is present in the development dependencies."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert (
            "ruff>=0.15.8"
            in pyproject_contents["project"]["optional-dependencies"]["dev"]
        )


class TestGettingPyprojectProjectMetadata:
    """Describe the project metadata declared in pyproject.toml."""

    def test_should_define_the_external_project_name(self) -> None:
        """Assert that the public project name is defined."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["project"]["name"] == "StratForge"
