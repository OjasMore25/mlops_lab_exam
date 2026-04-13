import json
import pickle
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

print("Training started...")

data = load_diabetes()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)

print("MSE:", mse)

# save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# save metrics
metrics = {"mse": mse}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print("Training finished. Model and metrics saved.")