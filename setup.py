# setup.py
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup()


"""
packages=find_packages(exclude=["tests", "tests.*", "migrations/*"]),
        include_package_data=True,  # Ensure MANIFEST.in is respected
        exclude_package_data={
            '': ['*.pyc', '*.pyo', '*.pyd', '**/migrations/*']  # Exclude .pyc, .pyo, .pyd files and migration files
        },
"""
