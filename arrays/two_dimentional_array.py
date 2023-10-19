import numpy as np

two_D_arr = np.array([],[])
coloumn1 = [1,2,3,4]
coloumn2 = [6,7,8,9]
new_2D_arr = np.insert(two_D_arr,0,coloumn1,axis=1)
new_2D_arr = np.insert(two_D_arr,1,coloumn2,axis=1)
print(new_2D_arr)