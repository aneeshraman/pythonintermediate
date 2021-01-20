import pandas as pd

sal = pd.read_csv(r"C:\Users\anees\Machine Learning\Pandas\Exercise\Salaries.csv")

var = sal.groupby(by="Year").mean()["BasePay"]


print(end='')
