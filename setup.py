"""Setuptools configuration for the StratForge package."""

import pathlib

import setuptools

README_PATH = pathlib.Path(__file__).parent / "README.md"


setuptools.setup(
    name="StratForge",
    version="0.0.1",
    description="Base package for the StratForge Python library.",
    long_description=README_PATH.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license_files=["LICENSE.md", "LICENSE-COMMERCIAL.md"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.14",
    install_requires=[],
    extras_require={"dev": ["pytest>=8.0", "pytest-cov>=6.0", "ruff>=0.15.8"]},
)
