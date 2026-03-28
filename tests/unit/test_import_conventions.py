"""Unit tests for the repository import conventions."""

import ast
import importlib.util
import pathlib


class TestGettingModuleOnlyImports:
    """Describe the repository module import convention."""

    def test_should_use_only_module_imports_in_source(self) -> None:
        """Assert that the source tree avoids direct symbol imports except for classproperty."""
        repository_root = pathlib.Path(__file__).resolve().parents[2]
        python_paths = sorted((repository_root / "src").rglob("*.py"))
        violating_imports: list[str] = []

        for python_path in python_paths:
            module_tree = ast.parse(python_path.read_text(encoding="utf-8"))

            for node in ast.walk(module_tree):
                if isinstance(node, ast.ImportFrom) and not self._is_allowed_module_import(node):
                    violating_imports.append(f"{python_path.relative_to(repository_root)}:{node.lineno}")

        assert violating_imports == []

    def test_should_use_only_module_imports_in_tests(self) -> None:
        """Assert that the tests tree avoids direct symbol imports except for classproperty."""
        repository_root = pathlib.Path(__file__).resolve().parents[2]
        python_paths = sorted((repository_root / "tests").rglob("*.py"))
        violating_imports: list[str] = []

        for python_path in python_paths:
            module_tree = ast.parse(python_path.read_text(encoding="utf-8"))

            for node in ast.walk(module_tree):
                if isinstance(node, ast.ImportFrom) and not self._is_allowed_module_import(node):
                    violating_imports.append(f"{python_path.relative_to(repository_root)}:{node.lineno}")

        assert violating_imports == []

    @classmethod
    def _is_allowed_module_import(cls, node: ast.ImportFrom) -> bool:
        """Return whether an import-from statement only imports modules or the classproperty exception."""
        if node.module is None:
            return False

        return all(cls._is_allowed_import_name(node.module, imported_name.name) for imported_name in node.names)

    @classmethod
    def _is_allowed_import_name(cls, module_name: str, imported_name: str) -> bool:
        """Return whether the imported name is an allowed module import."""
        if module_name == "strat_forge" and imported_name == "classproperty":
            return True

        return importlib.util.find_spec(f"{module_name}.{imported_name}") is not None
