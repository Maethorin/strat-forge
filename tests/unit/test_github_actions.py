"""Unit tests for the GitHub Actions workflow contract."""

from pathlib import Path


class TestGettingContinuousIntegrationWorkflow:
    """Describe the repository continuous integration workflow contract."""

    def test_should_define_a_ci_workflow(self) -> None:
        """Assert that the repository exposes a CI workflow file."""
        workflow_path = (
            Path(__file__).resolve().parents[2] / ".github" / "workflows" / "ci.yml"
        )

        assert workflow_path.is_file()

    def test_should_run_tests_with_coverage_and_upload_to_codecov(self) -> None:
        """Assert that the CI workflow generates coverage and uploads it to Codecov."""
        workflow_path = (
            Path(__file__).resolve().parents[2] / ".github" / "workflows" / "ci.yml"
        )
        workflow_contents = workflow_path.read_text(encoding="utf-8")

        assert "pytest --cov=strat_forge --cov-report=xml" in workflow_contents
        assert "codecov/codecov-action" in workflow_contents
        assert "files: ./coverage.xml" in workflow_contents
