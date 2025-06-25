import numpy as np 

a = np.array([[1,2],[3,np.nan],[np.nan,5],[np.nan,np.nan]])
print(a)
b = a[:,0] + a[:,1]
print(b)
c = np.array([True,False, False, False])
print(c)
print(np.sum(c))
print(np.count_nonzero(c))