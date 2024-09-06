#!/bin/bash

# Check for environment argument
if [ $# -eq 0 ]; then
    echo "No environment specified. Usage: $0 <environment>"
    echo "Example: $0 test"
    exit 1
fi

ENVIRONMENT=$1

# Remove the existing distribution directory
echo "Removing existing distribution directory..."
rm -rf dist/

# Clean bdist wheel
echo "Cleaning build directory..."
python setup.py clean --all bdist_wheel

# Build the source distribution
echo "Building the source distribution..."
python setup.py sdist

# Build the wheel distribution
echo "Building the wheel distribution..."
python setup.py bdist_wheel

# Upload distributions based on environment
if [ "$ENVIRONMENT" = "test" ]; then
    echo "Uploading distributions to TestPyPI..."
    python3 -m twine upload --repository testpypi dist/*
elif [ "$ENVIRONMENT" = "live" ]; then
    echo "Uploading distributions to PyPI..."
    python3 -m twine upload dist/*
else
    echo "Unknown environment: $ENVIRONMENT"
    echo "Valid options are: test, live"
    exit 1
fi

# Clean up
echo "Cleaning up temporary files..."
rm -rf build/  # Remove build directory
rm -rf *.egg-info/  # Remove egg-info directory
