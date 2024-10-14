# Linear Regression Analysis on Car and Oil Filter Sales

This project performs a linear regression analysis to investigate the relationship between new car sales and oil filter sales, while accounting for potential outliers in the data.

## Overview

The code processes sales data for two variables:
- **New car sales**
- **Oil filter sales**

The goal is to model the relationship between these two variables using linear regression. Outliers in oil filter sales are identified and removed before fitting the model to ensure a more accurate analysis.

## Features

- Data preprocessing to handle potential outliers.
- Z-score based method for outlier detection.
- Linear regression modeling using `scikit-learn` to predict oil filter sales based on new car sales.
- Calculation of the regression equation and R-squared value to evaluate model performance.

## Data

The input dataset includes the following columns:

| Season | New Car Sales (in millions) | Oil Filter Sales (in thousands) |
|--------|-----------------------------|---------------------------------|
| 1      | 2.45                        | 10.10                           |
| 2      | 2.70                        | 9.75                            |
| 3      | 2.20                        | 10.10                           |
| 4      | 2.85                        | 10.90                           |
| 5      | 3.10                        | 8.70                            |
| 6      | 2.90                        | 11.70                           |
| 7      | 3.20                        | 12.50                           |
| 8      | 2.50                        | 11.50                           |
| 9      | 2.75                        | 13.00                           |

## Steps

1. **Data Loading**: The dataset is loaded as a NumPy array.
2. **Outlier Detection**: Z-scores for oil filter sales are calculated, and any values with a Z-score greater than 3 are considered outliers and removed.
3. **Linear Regression**: A linear regression model is trained on the cleaned data using new car sales as the predictor and oil filter sales as the response variable.
4. **Results**: The regression equation and the R-squared value (model accuracy) are printed.

## Output

The program outputs:
- The linear regression equation in the form: `y = slope * x + intercept`
- The R-squared value to indicate the goodness of fit.

Example:
```
Linear Regression Equation: y = 2.0571x + 4.1938
R-squared: 0.9324
```

## Requirements

- Python 3.x
- NumPy
- SciPy
- scikit-learn

Install the required libraries using pip:
```bash
pip install numpy scipy scikit-learn
```

## Usage

Run the script:
```bash
python src/yin_guo_guan_xi/linear_regression_analysis.py
```

## License

This project is licensed under the MIT License.