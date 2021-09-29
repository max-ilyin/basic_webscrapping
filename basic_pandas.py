import pandas as pd

df = pd.read_csv('datasets/BankChurners 2.csv')
# datasets dowloaded from https://www.kaggle.com/sakshigoyal7/credit-card-customers

dependent_count_0 = df[(df["Dependent_count"] == 0)]
dependent_count_1 = df[(df["Dependent_count"] == 1)]
dependent_count_2 = df[(df["Dependent_count"] == 2)]
dependent_count_3 = df[(df["Dependent_count"] == 3)]
dependent_count_4 = df[(df["Dependent_count"] == 4)]
dependent_count_5 = df[(df["Dependent_count"] == 5)]

print(len(dependent_count_0))
print(len(dependent_count_1))
print(len(dependent_count_2))
print(len(dependent_count_3))
print(len(dependent_count_4))
print(len(dependent_count_5))

dependent_count_0.to_csv("dependent_count0.csv")