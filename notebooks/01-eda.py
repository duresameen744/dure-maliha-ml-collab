# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw/adult.csv")
df.shape

# %%
df.head()

# %%
print("Missing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# %%
df["class"].value_counts(normalize=True)

# %%
df["class"].value_counts().plot(kind="bar", title="Income class distribution")
plt.show()

# %%
df[["age", "hours-per-week", "education-num"]].hist(figsize=(10, 4))
plt.tight_layout()
plt.show()

# %%
import sys

sys.path.append("..")
from src.data_cleaning import clean_adult_data

df_clean = clean_adult_data(df)
print(f"Before: {df.shape[0]} rows -> After: {df_clean.shape[0]} rows")

# %%

# %%
