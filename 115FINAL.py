import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = pd.read_excel(r"C:\Users\msu-wone\Documents\ISY115_binned123.xlsx")

data = data[["age", "gender", "stress_level", "anxiety_score", "depression_score", "mental_health_risk"]]

print(data.head())



from sklearn.model_selection import train_test_split

X = data[["age", "gender", "stress_level", "anxiety_score", "depression_score"]]
y = data["mental_health_risk"]

X_train, X_temp, y_train, y_temp = train_test_split(
X, y, test_size=0.30, random_state=42, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

print("Training size:", len(X_train))
print("Validation size:", len(X_val))
print("Testing size:", len(X_test))


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

val_pred = model.predict(X_val)
print("Validation results")
print(classification_report(y_val, val_pred))

test_pred = model.predict(X_test)
print("Test results")
print(classification_report(y_test, test_pred))

print(data.groupby("mental_health_risk")["age"].mean())

print(data.groupby("mental_health_risk")["gender"].value_counts())


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# predictions already computed
test_accuracy = accuracy_score(y_test, test_pred)
test_precision = precision_score(y_test, test_pred, average="weighted")
test_recall = recall_score(y_test, test_pred, average="weighted")
test_f1 = f1_score(y_test, test_pred, average="weighted")

table = pd.DataFrame({
    "MODEL": ["Decision Tree"],
    "ACCURACY": [round(test_accuracy, 3)],
    "PRECISION": [round(test_precision, 3)],
    "RECALL": [round(test_recall, 3)],
    "F1_SCORE": [round(test_f1, 3)]
})

print(table)


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

val_accuracy = accuracy_score(y_val, val_pred)
val_precision = precision_score(y_val, val_pred, average="weighted")
val_recall = recall_score(y_val, val_pred, average="weighted")
val_f1 = f1_score(y_val, val_pred, average="weighted")

test_accuracy = accuracy_score(y_test, test_pred)
test_precision = precision_score(y_test, test_pred, average="weighted")
test_recall = recall_score(y_test, test_pred, average="weighted")
test_f1 = f1_score(y_test, test_pred, average="weighted")

table = pd.DataFrame({
    "MODEL": ["Decision Tree", "Decision Tree"],
    "DATASET": ["Validation", "Test"],
    "ACCURACY": [round(val_accuracy, 3), round(test_accuracy, 3)],
    "PRECISION": [round(val_precision, 3), round(test_precision, 3)],
    "RECALL": [round(val_recall, 3), round(test_recall, 3)],
    "F1_SCORE": [round(val_f1, 3), round(test_f1, 3)]
})

print(table)


# print("Correlation matrix")
# print(data.corr())

# print("\nScore ranges per risk group")
# print(data.groupby("mental_health_risk")[["stress_level", "anxiety_score", "depression_score"]].agg(["min", "max"]))
#
# print("\nUnique combinations of scores and risk")
# print(data.groupby(["stress_level", "anxiety_score", "depression_score"])["mental_health_risk"].nunique().value_counts())


# from sklearn.metrics import confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# val_cm = confusion_matrix(y_val, val_pred)
#
# plt.figure(figsize=(5,4))
# sns.heatmap(val_cm, annot=True, fmt="d")
# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.title("Validation Confusion Matrix")
# plt.show()
#
# test_cm = confusion_matrix(y_test, test_pred)
#
# plt.figure(figsize=(5,4))
# sns.heatmap(test_cm, annot=True, fmt="d")
# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.title("Test Confusion Matrix")
# plt.show()

# import shap
# import pandas as pd
#
# explainer = shap.TreeExplainer(model)
# shap_values = explainer.shap_values(X_train)
#
# shap.summary_plot(shap_values, X_train, plot_type="bar")
# shap.summary_plot(shap_values, X_train)

# import shap
# import matplotlib.pyplot as plt
#
# explainer = shap.TreeExplainer(model)
# shap_values = explainer.shap_values(X_train)
#
# shap.summary_plot(shap_values, X_train)