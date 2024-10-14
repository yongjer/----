import numpy as np
from scipy import stats

# Load the data (season, new car sales, oil filter sales)
data = np.array([
    [1, 2.45, 10.10],
    [2, 2.70, 9.75],
    [3, 2.20, 10.10],
    [4, 2.85, 10.90],
    [5, 3.10, 8.70],
    [6, 2.90, 11.70],
    [7, 3.20, 12.50],
    [8, 2.50, 11.50],
    [9, 2.75, 13.00]
])
# Extract new car sales and oil filter sales
new_car_sales = data[:, 1]
oil_filter_sales = data[:, 2]

# Calculate Z-scores
z_scores = np.abs(stats.zscore(oil_filter_sales))

# Define threshold (typically 3)
threshold = 3

# Find indices of non-outliers
non_outlier_indices = np.where(z_scores < threshold)[0]

# Remove outliers
data_without_outliers = data[non_outlier_indices]

from sklearn.linear_model import LinearRegression

# Extract X (new car sales) and y (oil filter sales) from the data without outliers
X = data_without_outliers[:, 1].reshape(-1, 1)
y = data_without_outliers[:, 2]

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients (slope and intercept)
slope = model.coef_[0]
intercept = model.intercept_

print(f"Linear Regression Equation: y = {slope:.4f}x + {intercept:.4f}")
print(f"R-squared: {model.score(X, y):.4f}")