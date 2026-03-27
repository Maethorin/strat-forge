"""Unit tests for the project README contract."""

from pathlib import Path


class TestGettingReadmeBadges:
    """Describe the badge contract exposed at the top of the README."""

    def test_should_define_a_single_badge_line_below_the_title(self) -> None:
        """Assert that the README exposes the required minimal badge line."""
        readme_path = Path(__file__).resolve().parents[2] / "README.md"
        readme_lines = readme_path.read_text(encoding="utf-8").splitlines()

        assert readme_lines[0] == "# StratForge"
        assert "[![Build Status]" in readme_lines[2]
        assert "[![Coverage]" in readme_lines[2]
        assert "[![License]" in readme_lines[2]
        assert "[![Python]" in readme_lines[2]
        assert "license-Non--Commercial" in readme_lines[2]

    def test_should_only_expose_the_required_badges(self) -> None:
        """Assert that the README keeps the badge row limited to the required badges."""
        readme_path = Path(__file__).resolve().parents[2] / "README.md"
        badge_line = readme_path.read_text(encoding="utf-8").splitlines()[2]

        assert badge_line.count("[![") == 4
        assert "downloads" not in badge_line.lower()
        assert "activity" not in badge_line.lower()
        assert "commits" not in badge_line.lower()
        assert "unspecified" not in badge_line.lower()


class TestGettingReadmeLicenseSection:
    """Describe the README license section contract."""

    def test_should_describe_the_non_commercial_license_terms(self) -> None:
        """Assert that the README reflects the repository license summary."""
        readme_path = Path(__file__).resolve().parents[2] / "README.md"
        readme_contents = readme_path.read_text(encoding="utf-8")

        assert "non-commercial use" in readme_contents.lower()
        assert "commercial license" in readme_contents.lower()
        assert "see LICENSE" in readme_contents
        assert "LICENSE-COMMERCIAL.md" in readme_contents
