import numpy as np

# ex 1

# bu masalada sort() metodi bilan arraylarni tartiblayabmiz

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))


# ex 2

# bu masalada so'zlarni tartiblash ko'rsatilyabdi alifbo tartibida saralanadi

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))


# ex 3

# bu masalada mantiqiy qiymatlar saralanmoqda 

arr = np.array([True, False, True])

print(np.sort(arr))

# ex 4

# bu masalada 2D massiv saralanyabdi bu joyda 2d massivning har bir massivi saralanadi

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))