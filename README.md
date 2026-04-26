# TMDB Box Office Prediction
**Daniele Buono (0001180817)**

This repository contains the project work developed for the **Machine Learning and Data Mining** course at the **University of Bologna**. The goal of the project is to predict the worldwide revenue of movies using data from the TMDB (The Movie Database) competition.

---

## References & Tools
* **Competition**: [Kaggle TMDB Box Office Prediction](https://www.kaggle.com/competitions/tmdb-box-office-prediction)
* **Institution**: Alma Mater Studiorum – Università di Bologna
* **Stack**: Python (`pandas`, `matplotlib`, `numpy`, `sklearn`, `seaborn`, `xgboost`, `ast`, `wordcloud`, `lightgbm`, `catboost`)

---

## Project Overview
The film industry is a high-stakes business where predicting a movie's financial success is crucial. This project explores various features—from budgets and genres to cast and crew—to build a predictive model for box office revenue.

### Objectives
* Perform an in-depth **Exploratory Data Analysis (EDA)** to find key revenue drivers.
* Clean and transform complex, nested JSON data into usable features.
* Implement and tune advanced Regression models.
* Optimize performance based on the **RMSLE** (Root Mean Squared Logarithmic Error) metric.

---

### Project Structure
The project is organized into two main Jupyter notebooks:

#### 1. Exploratory Data Analysis (EDA)
- Dataset inspection
- Distribution analysis of target and features
- Correlation analysis and feature relationships
- Visualization of categorical variables (genres, production companies, cast, ...)

#### 2. Feature Engineering & Model Tuning
- Parsing nested JSON-like fields (genres, cast, crew, production companies)
- Handling missing values and skewed distributions
- Feature transformations (log scaling, encoding, aggregation)
- Temporal feature extraction (release year, month, seasonality)
- Feature selection and dimensionality reduction
- Baseline models
- Model training and hyperparameter optimization (Random Forest, XGBoost, LightGBM, CatBoost)
- Final prediction and submission generation

```project-root/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── sample_submission.csv
│   └── submission.csv
│
├── src/
│   ├── eda.ipynb
│   └── prediction.ipynb
│   └── utils.py
│
├── setup.sh
└── README.md
```


---

### Results

The models were evaluated using both **R² score** and **RMSLE (Root Mean Squared Logarithmic Error)**.

| Model | RMSLE | R² Score |
| :--- | :---: | :---: |
| Baseline - Dummy Mean | 2.991 | -0.004 |
| Baseline - Dummy Median | 3.027 | -0.028 |
| Random Forest Regressor | 2.049 | 0.529 |
| LightGBM | 2.039 | 0.533 |
| XGBoost | 1.978 | 0.560 |
| CatBoost | **1.961** | **0.568** |

#### Key Findings

- The baseline models (mean and median predictors) perform poorly, confirming that the problem is non-trivial and requires non-linear modeling.
- All gradient boosting models significantly outperform Random Forest, both in terms of RMSLE and R².
- **CatBoost achieves the best overall performance**, obtaining:
  - the lowest RMSLE (**1.961**)
  - the highest R² score (**0.568**)

This indicates that CatBoost provides the best trade-off between predictive accuracy and generalization on this dataset, likely due to its strong handling of categorical-like feature interactions and robust gradient boosting implementation.

---

## Requirements
The project is built using **Python 3.13** and utilizes a variety of data science and visualization libraries. 

### Core Dependencies
* **Data Manipulation**: `pandas`, `numpy`
* **Machine Learning**: `scikit-learn`, `xgboost`
* **Data Visualization**: `matplotlib`, `seaborn`, `wordcloud`
* **Utilities**: `ast` (for literal evaluation of nested string data)

## Getting Started

To ensure a consistent environment and avoid dependency conflicts, it is recommended to use a virtual environment. I have provided a `setup.sh` script to automate this process.

### Automated Setup
The `setup.sh` script will automatically create a Python virtual environment, upgrade `pip`, and install all necessary libraries.

1.  **Give execution permissions to the script:**
    ```bash
    chmod +x setup.sh
    ```
2.  **Run the script:**
    ```bash
    ./setup.sh
    ```
3.  **Activate the environment:**
    ```bash
    source venv/bin/activate
    ```

### Manual Execution
If you prefer not to use the script, you can set up the project manually:
```bash
# Create the virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install pandas numpy scikit-learn xgboost matplotlib seaborn wordcloud lightgbm catboost