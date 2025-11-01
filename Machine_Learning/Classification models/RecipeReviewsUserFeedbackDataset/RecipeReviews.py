# importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# importing csv
Recipe = pd.read_csv("Machine_Learning/Classification models/RecipeReviewsUserFeedbackDataset/RecipeReviewsUserFeedbackDataset.csv")
print(Recipe)
print(Recipe.dtypes)
print(Recipe.describe())
print(Recipe["stars"].unique())

df = Recipe.select_dtypes(include=["int64", "float64"]) # as dataframe includes text columns also
print(df.corr())

# Cleaning data
Recipe = Recipe.drop_duplicates()
print(Recipe.isnull().sum())
Recipe = Recipe.fillna(0)

# Selecting feature column & label
feature_cols = Recipe[["user_reputation", "reply_count", "thumbs_up", "thumbs_down", "best_score"]]
x = feature_cols
y = Recipe.stars

# studying relationship between label & feature columns

print(Recipe["stars"].value_counts(normalize=True))
''' stars
5    0.760587
0    0.093279
4    0.091024
3    0.026950
1    0.015400
2    0.012760

This result is showing that label data is imbalanced because 5 star rating has 76% and all others are less than 10%'''

for m in x:
    sns.regplot(data=Recipe, x=m, y=y).set(title=f"Regression Plot of {m} and {y}")
    plt.show()
''' regression plot showing data is not linear'''

for m in x:
    sns.boxplot(data=Recipe, x=m, y=y).set(title=f"Box Plot of {m} and {y}")
    plt.show()

    
# Spliting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=16)

# Fitting Model
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import metrics

Models = {"Logistic Regression": LogisticRegression(),
          "Decision Tree": DecisionTreeClassifier(),
          "SVM": SVC()}

for name , model in Models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f" ------ {name} --------")
    print("Confusion Metrics:", metrics.confusion_matrix(y_test, y_pred))
    print("Acuuracy Score:", metrics.accuracy_score(y_test, y_pred))
    print("Classification Report:", metrics.classification_report(y_test,y_pred))

    cm = metrics.confusion_matrix(y_test,y_pred)

    sns.heatmap(cm, annot=True, fmt='d').set_title(f'Confusion matrix of {name}') # fmt='d' formats the numbers as digits, which means integers
    plt.show() 