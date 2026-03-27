"""Unit tests for the project pyproject configuration."""

from pathlib import Path
import tomllib

from strat_forge import __version__


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

    def test_should_include_pytest_in_the_dev_dependencies(self) -> None:
        """Assert that Pytest is present in the development dependencies."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert (
            "pytest>=8.0"
            in pyproject_contents["project"]["optional-dependencies"]["dev"]
        )

    def test_should_include_pytest_cov_in_the_dev_dependencies(self) -> None:
        """Assert that pytest-cov is present in the development dependencies."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert (
            "pytest-cov>=6.0"
            in pyproject_contents["project"]["optional-dependencies"]["dev"]
        )


class TestGettingPyprojectProjectMetadata:
    """Describe the project metadata declared in pyproject.toml."""

    def test_should_define_the_external_project_name(self) -> None:
        """Assert that the public project name is defined."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["project"]["name"] == "StratForge"

    def test_should_define_the_same_version_as_the_package(self) -> None:
        """Assert that pyproject.toml stays aligned with the package version."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["project"]["version"] == __version__

    def test_should_define_the_expected_python_version_requirement(self) -> None:
        """Assert that pyproject.toml declares the supported Python version."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["project"]["requires-python"] == ">=3.14"

    def test_should_define_the_license_file_as_project_metadata(self) -> None:
        """Assert that pyproject.toml exposes the repository license file."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["project"]["license"] == {"file": "LICENSE"}

    def test_should_define_both_repository_license_files(self) -> None:
        """Assert that pyproject.toml exposes both repository license files."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["project"]["license-files"] == [
            "LICENSE",
            "LICENSE-COMMERCIAL.md",
        ]

    def test_should_define_the_src_layout_wheel_package(self) -> None:
        """Assert that pyproject.toml points the wheel build to the src package."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["tool"]["hatch"]["build"]["targets"]["wheel"] == {
            "packages": ["src/strat_forge"]
        }


class TestGettingPyprojectPytestConfiguration:
    """Describe the pytest configuration declared in pyproject.toml."""

    def test_should_define_the_tests_directory_as_the_test_path(self) -> None:
        """Assert that pytest is configured to collect tests from the tests directory."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["tool"]["pytest"]["ini_options"]["testpaths"] == [
            "tests"
        ]

    def test_should_define_the_src_directory_in_the_python_path(self) -> None:
        """Assert that pytest is configured to import the src-layout package."""
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject_contents = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

        assert pyproject_contents["tool"]["pytest"]["ini_options"]["pythonpath"] == [
            "src"
        ]
