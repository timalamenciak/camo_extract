"""Setup for causal graph extractor."""

from setuptools import setup, find_packages

setup(
    name="causal-extractor",
    version="0.1.0",
    description="Extract causal graphs from PDF scientific articles",
    author="Tim Alamenciak",
    author_email="tim.alamenciak@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pydantic>=2.0",
        "pyyaml>=6.0",
        "requests>=2.31",
        "python-dotenv>=1.0",
    ],
    extras_require={
        "pdf": ["marker-pdf>=1.0"],
        "ontology": ["ontology-agent>=0.1.0"],
        "dev": [
            "ruff>=0.1.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "causal-extract=src.main:main",
        ],
    },
    python_requires=">=3.10",
)
