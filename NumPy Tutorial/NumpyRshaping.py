import numpy as np


# ex 1
# bu yerda 1d massivni har birida 3 tadan  elementi bor bo'lgan 4 ta massivga ega bo'lgan 2d massivga ajratyabmiz

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)



# ex 2

# bu esa 1d ni 3d qilish

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

# 2d ga -1 bersak 1d bo'lib qolishi mumkin

