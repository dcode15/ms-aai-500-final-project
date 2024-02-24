# AAI-500 Final Project

### Authors

- Edwin Merchan
- Prema Mallikarjunan
- Douglas Code

### Overview

This repository contains code for explanatory data analysis and modeling on the ACI dataset of climate metrics collected
in the United States and Canada.

### Environment Setup

All required packages are listed in `requirements.txt`. They can be installed with:

    pip install -r requirements.txt

### Project Layout

All Python files for the project are found in the `scripts` directory.

- data_cleanup: The script used for initial data cleaning
- cdd_eda: The code used for the exploratory data analysis portion of the project
- cdd_model: The code used for the modeling portion of the project
- rx5day_analysis, sea_level_analysis: Preliminary EDA scripts for exploring variables prior to choosing to examine consecutive dry days (CDD)

The original dataset, broken out tables, and final cleaned dataset can be found in the `data` directory.