import pandas as pd

df_with_nan = pd.DataFrame({
    'Name': ['A', 'B', None],
    'marks': [90,  None, 65]
})


print(df_with_nan.isnull())
print(df_with_nan.notnull())
print(df_with_nan.fillna(0))