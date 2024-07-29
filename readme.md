# Rule Engine Application

## Overview

This is a simple 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, spend, etc. The system uses Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## File Structure

- `app/`: Contains the application logic.
  - `models.py`: Defines the Node data structure.
  - `rule_parser.py`: Contains functions to parse and create rules.
  - `rule_evaluator.py`: Contains functions to evaluate rules.
  - `api.py`: Defines the API endpoints.
- `tests/`: Contains test cases for the rule engine.
- `main.py`: Entry point for running the Flask application.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Setup

1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
