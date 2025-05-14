# model_pipeline.py
# XGBoost model training for Federal Health IT award prediction

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load cleaned data
df = pd.read_csv("data/health_it_cleaned.csv")

# Basic preprocessing (example only)
df['log_award'] = np.log1p(df['award_amount'])
X = pd.get_dummies(df.drop(columns=['award_amount', 'log_award', 'award_id', 'start_date', 'end_date']))
y = df['log_award']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
print("R² Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "outputs/xgb_model.pkl")
