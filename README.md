# PREDIX

## Overview

PREDIX is an AI-based intelligent food packaging material recommendation system designed as a decision-support platform.

## Problem Statement

Food packaging selection depends on food properties, storage and transport conditions, packaging-material performance, and compatibility constraints.

## Solution

PREDIX uses a hybrid intelligent architecture that combines domain-knowledge feasibility checks with machine-learning-based ranking and explainable outputs.

## Architecture

Input -> analysis -> requirements -> compatibility -> ranking -> shelf-life/cost/sustainability -> recommendation

## Data Strategy

PREDIX separates:

1. Food-property data
2. Packaging-material data
3. Domain knowledge and literature-backed guidance
4. Future model training data

Data and science principles:

- No classified or private data should be used.
- Scientific values must be source-backed.
- Synthetic data may be used for prototype demonstrations.
- Final commercial packaging decisions require expert and laboratory validation.

## Technology Stack

Initial prototype:

- Python
- Pandas
- NumPy
- scikit-learn
- XGBoost
- Plotly
- Streamlit
- SQLite initially, with PostgreSQL as a scalable future option

## Status

🚧 Architecture / prototype development
