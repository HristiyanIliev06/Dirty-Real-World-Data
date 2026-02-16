import numpy as np
import pandas as pd

data = pd.read_csv("churn-analysis/data/raw/telco_churn.csv")

total_charges = pd.to_numeric(data["TotalCharges"], errors="coerce")
print(total_charges.isnull().sum())

