import pandas as pd

df = pd.read_csv('datasets/BankChurners 2.csv')
# datasets dowloaded from https://www.kaggle.com/sakshigoyal7/credit-card-customers

for count in range(6):
    dependent_count = df[(df["Dependent_count"] == count)]
    dependent_count.to_csv(f"results/dependent_count{count}.csv")