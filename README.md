# TMDB Box Office Prediction
**Daniele Buono (0001180817)**

This repository contains the project work developed for the **Machine Learning and Data Mining** course at the **University of Bologna**. The goal of the project is to predict the worldwide revenue of movies using data from the TMDB (The Movie Database) competition.

---

## References & Tools
* **Competition**: [Kaggle TMDB Box Office Prediction](https://www.kaggle.com/competitions/tmdb-box-office-prediction)
* **Institution**: Alma Mater Studiorum – Università di Bologna
* **Stack**: Python (`pandas`, `matplotlib`, `numpy`, `sklearn`, `seaborn`, `xgboost`, `ast`, `wordcloud`)

---

## Project Overview
The film industry is a high-stakes business where predicting a movie's financial success is crucial. This project explores various features—from budgets and genres to cast and crew—to build a predictive model for box office revenue.

### Objectives
* Perform an in-depth **Exploratory Data Analysis (EDA)** to find key revenue drivers.
* Clean and transform complex, nested JSON data into usable features.
* Implement and tune advanced Regression models.
* Optimize performance based on the **RMSLE** (Root Mean Squared Logarithmic Error) metric.

---

### Results
The models were evaluated based on their ability to minimize RMSLE

| Model | RMSLE | $R^2$ Score |
| :--- | :---: | :---: |
| **Random Forest Regressor** | 1.999 | 0.552 |
| **XGBoost Regressor** | **1.928** | **0.583** |

As shown in the evaluation, the **XGBoost Regressor** provided superior performance, achieving a lower error and a higher correlation with the actual revenue data.

---

### Project Structure
The notebook follows a standard machine learning pipeline:

1.  **Data Loading and Overview**: Initial inspection of the Kaggle dataset.
2.  **EDA (Exploratory Data Analysis)**: Visualizing the relationship between features and revenue, and analyzing categorical trends.
3.  **Feature Engineering**: 
    * Parsing nested dictionaries (Genres, Production Companies, Cast, ...).
    * Handling missing values and skewed distributions.
    * Date feature extraction (Release year, month, and seasonality).
    * Selecting the best K features to avoid overfitting
4.  **Model Tuning**: Comparing **Random Forest** and **XGBoost** through hyperparameter optimization.
5.  **Prediction and Submit**: Generating the final output for the competition leaderboard.

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
pip install pandas numpy scikit-learn xgboost matplotlib seaborn wordcloud