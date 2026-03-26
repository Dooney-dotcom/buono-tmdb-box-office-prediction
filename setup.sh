#!/bin/bash
set -e

ENV_NAME="myenv"

echo "Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python found: $PYTHON_VERSION"

echo "Checking venv..."

if ! python3 -m venv --help &> /dev/null; then
    echo "Venv module is not available."
    exit 1
fi

echo "Creating virtual environment: $ENV_NAME"
python3 -m venv $ENV_NAME

echo "Activating virtual environment..."
source $ENV_NAME/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing libraries..."

pip install pandas matplotlib numpy seaborn scikit-learn xgboost wordcloud

echo "Installation completed successfully!"

echo ""
echo "To activate the virtual environment in the future, run:"
echo "   source $ENV_NAME/bin/activate"