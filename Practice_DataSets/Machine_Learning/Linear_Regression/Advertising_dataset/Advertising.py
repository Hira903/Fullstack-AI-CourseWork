# %%
# importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# importing dataset usung pandas

Advertisment = pd.read_csv("advertising.csv")

print(Advertisment)

# %%
# exploring dataset
print("Columns in dataset are:", Advertisment.columns)
print(len(Advertisment["TV"]))
print(len(Advertisment["Radio"]))
print(len(Advertisment["Newspaper"]))
print(len(Advertisment["Sales"]))

# %%
# Checking for outliners

feature_cols = Advertisment[["TV", "Radio", "Newspaper"]]
x = feature_cols
y = Advertisment.Sales

print(x.shape)
print(y.shape)




# %%
for cols in x:
    sns.regplot(x=cols, y=y, data=Advertisment).set(title=f'Regression plot of {x} and {y}');
    plt.show()

for cols in x:
    sns.lineplot(x=cols, y=y, data=Advertisment).set(title=f'Line plot of {x} and {y}');
    plt.show()

# %%
# fitting linear regression model
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=25)

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error

Models = {"Linear Regression": LinearRegression(),
          "Ridge Regression": Ridge(),
          "Lasso Regression": Lasso()}

for names, model in Models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)


    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r_score = r2_score(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)

    print (f"---- {names} -----")
    print(f'Mean absolute error: {mae:.2f}')
    print(f'Mean squared error: {mse:.2f}')
    print(f'R2_Score: {r_score}')
    print(f'Root Mean Square error: {rmse:.2f}\n')


