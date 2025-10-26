# import Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading data
data = pd.read_csv("D:\GitHub\Fullstack-AI-CourseWork\Practice_DataSets\Machine_Learning\Classification models\StudentsDropout_AcademicSuccess\data.csv" , delimiter=";", index_col=1)

# exploring data using pandas functions
print("DataSet \n", data)
print("First 10 rows of dataset \n", data.head(10))
print("Last 10 rows of dataset \n", data.tail(10))
print("Information about dataset \n", data.info())
print("Shape of dataset \n", data.shape)
print("Columns of dataset \n", data.columns)
print("Statistical analysis \n", data.describe())


# exploring categories in Label column
print("Unique values in target column\n", data["Target"].unique())

# Converting Target column into integer
import sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data["target_encoded"] = le.fit_transform(data["Target"])

""" Target labels mapping: {'Dropout': np.int64(0), 'Enrolled': np.int64(1), 'Graduate': np.int64(2)}"""

print("Target labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(data[['Target', 'target_encoded']].head())

# Data Cleaning & studing through seaborn 
data = data.drop_duplicates()
print(data.shape)
print(data.head())
print(data.columns)
print(data.dtypes)

data_numeric = data.select_dtypes(include=["int","float"])
print(data_numeric.shape)
print(data_numeric.head())
print(data_numeric.columns)
print(data_numeric.dtypes)


# Selecting x and y of dataset
x = data_numeric.drop(columns=['target_encoded'])
y = data_numeric.target_encoded

sns.heatmap(data_numeric.corr())
plt.title("Heatmap of Correlation Values")
plt.show()

# Scaling data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
X_scaled = scaler.transform(x.values)

# Spliting data 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, train_size=0.85, random_state=20)

# Fitting Model
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

Models = {"Logistic Regression": LogisticRegression(),
          "Decision Tree": DecisionTreeClassifier(),
          "SVM": SVC(kernel="rbf"),
          "K_neighbour": KNeighborsClassifier(n_neighbors=3)}

for name , model in Models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    print(f" ------ {name} --------")
    print("Confusion Metrics:", metrics.confusion_matrix(y_test, y_pred))
    print("Accuracy Score:", metrics.accuracy_score(y_test, y_pred))
    print("Classification Report:", metrics.classification_report(y_test,y_pred))

    cm = metrics.confusion_matrix(y_test,y_pred)

    sns.heatmap(cm, annot=True, fmt='d').set_title(f'Confusion matrix of {name}') # fmt='d' formats the numbers as digits, which means integers
    plt.show() 

