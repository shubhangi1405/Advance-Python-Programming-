import pandas as pd
import numpy as np

arr = np.random.randint(1, 100, 10)

s = pd.Series(arr)

print("Pandas Series:")
print(s)
