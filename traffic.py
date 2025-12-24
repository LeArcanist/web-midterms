import pandas as pd

df = pd.read_csv("traffic_accidents.csv")
df_10k = df.head(10000)
df_10k.to_csv("traffic_accidents_10k.csv", index=False)
