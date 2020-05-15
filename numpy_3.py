import numpy as np
import pandas as pd
t1 = np.array(range(1,10)).reshape(3,3)
# print(t1)
# print(t1[:2])
# print(t1[0:2,0:2])
# print(t1[1,0:2])
# print(t1.T)
arr = pd.Series([25,14,36,89,44,82,89],index=['a','b','c','d','e','f','g'])
print(arr[0:6:2])
