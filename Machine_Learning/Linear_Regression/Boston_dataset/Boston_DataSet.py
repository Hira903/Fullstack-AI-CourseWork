# %%
# importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# loading dataset from CSV file using pandas
boston = pd.read_csv("Machine_Learning\Linear_Regression\Boston_dataset\Boston.csv")
print(boston)

# %%
# exploring dataset
print("printing first 5 rows", boston.head())
print("printing last 5 rows", boston.tail())
print("printing info", boston.info())
print("Statistical analysis:", boston.describe().T)
print("Calculating coorelation",boston.corr())


# %%
# Selecting feature columns & target columns
feature_cols = boston[["crim", "zn", "indus", "chas", "nox", "rm", "age", "dis", "rad", "tax", "ptratio"]]
x = feature_cols
y = boston["medv"]


# %%
# exploring data through visualizing
for cols in x:
    sns.regplot(x=cols, y=y, data=boston).set(title=f'Regression plot of {x} and {y}');
    plt.show()

for cols in x:
    sns.histplot(x=cols, y=y, data=boston, kde= True).set(title=f'Hist plot of {x} and {y}');
    plt.show()



# %%
sns.heatmap(boston.corr(), annot=True, cmap='coolwarm').set(title='Heat map of Boston_DataSet')
# Display the plot
plt.show()

sns.pairplot(boston).set(title='PearPlot of Boston_DataSet')
plt.show()



# %%
# Data cleaning 
# Removing outliners in column 'crim'
boston.loc[boston["crim"] >= 35]
boston["crim"] = boston["crim"] < 35



# %%
boston.loc[boston["crim"] >= 35]

# %%
boston.loc[boston["crim"] >= 60]
boston.corr()['medv'].sort_values(ascending=False)

# %%
# Selecting feature columns & target columns
feature_cols1 = boston[["crim", "zn", "indus", "nox", "rm", "age", "tax", "ptratio", "lstat", "dis", "rad"]]

x1 = feature_cols1
y1 = boston["medv"]


# %%
# importing libraries to train model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x1,
                                                                  y1,
                                                             train_size=.7,
                                                           random_state=25)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Transform features
X_test_scaled = scaler.transform(X_test)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train_scaled, y_train)
y_pred_reg = regressor.predict(X_test_scaled)

from sklearn.linear_model import Ridge
ridge = Ridge()
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
mae = mean_absolute_error(y_test, y_pred_reg)
mse = mean_squared_error(y_test, y_pred_reg)
r_score = r2_score(y_test, y_pred_reg)
rmse = root_mean_squared_error(y_test, y_pred_reg)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'R2_Score: {r_score}')
print(f'Root Mean Square error: {rmse:.2f}')

print()
print()

mae_r = mean_absolute_error(y_test, y_pred_ridge)
mse_r = mean_squared_error(y_test, y_pred_ridge)
r_score_r = r2_score(y_test, y_pred_ridge)
rmse_r = root_mean_squared_error(y_test, y_pred_ridge)

print(f'Mean absolute error of Ridge Model: {mae_r:.2f}')
print(f'Mean squared error of Ridge Model: {mse_r:.2f}')
print(f'R2_Score of Ridge Model: {r_score_r}')
print(f'Root Mean Square error of Ridge Model: {rmse_r:.2f}')






