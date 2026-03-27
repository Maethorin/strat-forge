"""Unit tests for the project setup module."""

from pathlib import Path


class TestGettingSetupConfiguration:
    """Describe the setup.py package configuration contract."""

    def test_should_define_src_layout_package_metadata(self) -> None:
        """Assert that setup.py exposes the expected package metadata."""
        setup_path = Path(__file__).resolve().parents[2] / "setup.py"

        assert setup_path.is_file()

        setup_contents = setup_path.read_text(encoding="utf-8")

        assert 'name="StratForge"' in setup_contents
        assert 'package_dir={"": "src"}' in setup_contents
        assert 'packages=find_packages(where="src")' in setup_contents
        assert 'python_requires=">=3.14"' in setup_contents
        assert '"ruff>=0.15.8"' in setup_contents
