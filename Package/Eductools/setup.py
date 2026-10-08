from setuptools import setup, find_packages

setup(
    name="Eductools",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy", "click"],
    extras_require={
        "dev": ["pytest"],
    },
    entry_points={
        "console_scripts": [
            "math=eductools_cli.math_tools_cli:calcul_cli",
        ],
    }
)