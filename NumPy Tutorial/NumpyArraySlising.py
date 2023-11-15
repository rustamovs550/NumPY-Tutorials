import numpy as np

# ex 1 
#bu yerda massivning 1 indexsidagi elementidan 5 chiindexsidagi elementgacha bo'lgan qiymatlar chop etiladi


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])



#ex 2

# bu yerda 4 chi elementdan oxirgi elementgacha qiymatlar chop etiladi 


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[4:])


#ex 3 


# bu yerda 0 chi elementdan 4 chi elementgacha qiymatlar chop etiladi 


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[:4])


# ex 4


# bu yerda 1 chi elementdan 5 chi elementgacha qiymatlar har 2 ta qadam bo'yicha chop etiladi 


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])






                                        # 2 D Arrays

# ex 1


# bu yerda 1 chi qatorning 1 chi elementdan 4 chi elementgacha qiymatlar  chop etiladi 


# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1, 1:4])


# ex 2

# bu yerda 0 chi qatordan 2 chi qatorgacha barcha qatorlarning 2 chi elementlari chop etilyabdi

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 2])



# ex 3

# bu yerda 0 chi qatordan 2 chi qatorgacha barcha qatorlarning 1 chi elementidan boshlab 4 chi elementigacha barcha  elementlari chop etilyabdi


# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 1:4])

                                                # 3 D massiv

import numpy as np

# 3D NumPy massivni yaratish (masalan)
arr_3d = np.array([
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    [[1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8], [1, 2,3,4,5,7,8]], 
    
    ])

# Qatorlarni o'qi bo'yicha va 1 chi elementidan 5 chi elementigacha qatorlarni tanlash
for i in range(1,6):  # 1 chi qatoridan 5 chi qatorigacha
    for j in range(1,6):  # 1 chi elementidan 5 chi elementigacha
        for k in range(1,6):
            print(f"3D massivning\nZ o'qi bo'yicha {i} qatorining,\nY o'qi bo'yicha {j} qatorining,\nX o'qi bo'yicha {k} chi elementi {arr_3d[i,j,k]} ga teng\n")