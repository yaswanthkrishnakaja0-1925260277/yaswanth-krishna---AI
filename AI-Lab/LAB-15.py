# 5. Decision Tree
# Install first: pip install scikit-learn
from sklearn.tree import DecisionTreeClassifier

X = [[1, 20], [2, 25], [7, 60], [8, 65]]
y = ["No", "No", "Yes", "Yes"]

model = DecisionTreeClassifier().fit(X, y)
print("Prediction:", model.predict([[3, 30]])[0])
