"""Unit tests for the project setup module."""

import pathlib
import re

import strat_forge


class TestGettingSetupConfiguration:
    """Describe the setup.py package configuration contract."""

    def test_should_define_src_layout_package_metadata(self) -> None:
        """Assert that setup.py exposes the expected package metadata."""
        setup_path = pathlib.Path(__file__).resolve().parents[2] / "setup.py"

        assert setup_path.is_file()

        setup_contents = setup_path.read_text(encoding="utf-8")

        assert 'name="StratForge"' in setup_contents
        assert 'package_dir={"": "src"}' in setup_contents
        assert 'packages=setuptools.find_packages(where="src")' in setup_contents
        assert 'python_requires=">=3.14"' in setup_contents
        assert '"ruff>=0.15.8"' in setup_contents
        assert '"pytest-cov>=6.0"' in setup_contents

    def test_should_define_the_same_version_as_the_package(self) -> None:
        """Assert that setup.py stays aligned with the package version."""
        setup_path = pathlib.Path(__file__).resolve().parents[2] / "setup.py"
        setup_contents = setup_path.read_text(encoding="utf-8")
        version_match = re.search(r'version="([^"]+)"', setup_contents)

        assert version_match is not None
        assert version_match.group(1) == strat_forge.__version__

    def test_should_read_the_readme_as_the_long_description(self) -> None:
        """Assert that setup.py uses the repository README as long description."""
        setup_path = pathlib.Path(__file__).resolve().parents[2] / "setup.py"
        setup_contents = setup_path.read_text(encoding="utf-8")

        assert 'README_PATH = pathlib.Path(__file__).parent / "README.md"' in setup_contents
        assert (
            'long_description=README_PATH.read_text(encoding="utf-8")' in setup_contents
        )

    def test_should_include_the_repository_license_file(self) -> None:
        """Assert that setup.py includes the repository license metadata."""
        setup_path = pathlib.Path(__file__).resolve().parents[2] / "setup.py"
        setup_contents = setup_path.read_text(encoding="utf-8")

        assert 'license_files=["LICENSE.md", "LICENSE-COMMERCIAL.md"]' in setup_contents
