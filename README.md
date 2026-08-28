# Bike Demand Prediction

A machine learning regression project that predicts the number of bike rentals based on weather conditions, calendar information, and time-related features.

## Live Demo

[Open the deployed Streamlit application](https://bike-demand-prediction-burhan.streamlit.app/)

## Project Overview

This project uses the Bike Sharing Demand dataset to build a regression model capable of predicting hourly bike rental demand.

The project covers the complete machine learning workflow:

* Data cleaning
* Exploratory Data Analysis
* Datetime feature extraction
* Train-test splitting
* Feature scaling
* Model comparison
* Hyperparameter tuning
* Final model training
* Prediction on unseen data
* Streamlit deployment

## Dataset

The dataset is provided through the Kaggle Bike Sharing Demand competition.

Dataset and competition:

https://www.kaggle.com/c/bike-sharing-demand

The dataset contains information about bike rental demand, including:

* Season
* Holiday
* Working day
* Weather
* Temperature
* Feeling temperature
* Humidity
* Windspeed
* Datetime

The target variable is:

`count` — total number of bike rentals.

The `casual` and `registered` columns were removed because they are not available in the competition test dataset and would not be appropriate as prediction features.

## Feature Engineering

The original `datetime` column was converted into useful time-based features:

* `year`
* `month`
* `day`
* `hour`
* `day_of_week`

These features allow the model to learn patterns related to time and bike demand.

## Models Compared

The following regression models were evaluated:

* Linear Regression
* Ridge Regression
* Decision Tree Regressor
* Gradient Boosting Regressor
* Random Forest Regressor

Random Forest achieved the best overall performance among the tested models.

## Model Evaluation

Models were evaluated using:

* RMSE (Root Mean Squared Error)
* R² Score
* Adjusted R² Score

Random Forest was then tuned using `GridSearchCV`.

The final model was selected based on validation RMSE.

## Hyperparameter Tuning

GridSearchCV was used to search through combinations of:

* `n_estimators`
* `max_depth`
* `min_samples_split`

Five-fold cross-validation was used during tuning.

## Streamlit Application

The trained Random Forest model is deployed through a Streamlit interface.

Users can provide:

* Date
* Time
* Season
* Holiday status
* Working day
* Weather condition
* Temperature
* Feeling temperature
* Humidity
* Windspeed

The application automatically extracts the required datetime features and returns the predicted number of bike rentals.

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

## Project Structure

```text
Bike Demand Prediction/
│
├── app.py
├── bike_demand_model.pkl
├── bike_expected_cols.pkl
├── notebook.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Run Locally

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Future Improvements

Possible improvements include:

* Time-based validation instead of a random train-test split
* Additional feature engineering
* Log transformation of the target variable
* Optimization specifically for RMSLE
* Testing additional regression algorithms
* Improved UI and prediction visualization

## Author

**Burhan Arshad**

Computer Science Student | Machine Learning Enthusiast
