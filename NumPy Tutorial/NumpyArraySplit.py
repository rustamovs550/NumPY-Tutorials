import numpy as np


# ex 1

# bu kod arr massivini 3 ta massivga ajratadi yani 1D massivni 2D massivga ajratadi bu massivni ichida 3ta massiv bo'ladi

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)


# ex 2

# bu kod arr massivini 4 ta massivga ajrat deyilyabdi lekin bizni massivimizni elementlari yetmaydi lekin array_split() metodi o'zi 
# bizga oxirini moslashtirib beradi
# split() bilan array_split() metodlarini asosiy farqi shunda 

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 4)

# print(newarr)


# ex 3

# bu misolda 2D massivni 3D massiv qilmoqda

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr)


# ex 4

# axis atributi bilan har bir massivning birinchi elementlarini yaratilyotgan elementning 1 massiving elementlari bo'lsin deyabmiz

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


# ex 5

# bu misolda hsplit() metodi berilgan u hstack() qanaqa vazifa bajarsa o'shani teskarisini bajaradi

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)