import numpy as np

l1 = np.array([1,2,3,4])
print(l1, l1.ndim)

l2 = np.array([[1,2,3],
               [4,5,6]])
print(l2,l2.ndim)

l3 = np.array(
    [
        [[1,2,3],
               [4,5,6]]
    ]
)
print(l3,l3.ndim)