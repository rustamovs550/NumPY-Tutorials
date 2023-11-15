import numpy as np


# ex 1

# concenate metodi bu metod default tarzda 2 ta massivni shunchaki qo'shib qo'yadi 3 chi massivga

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))

# print(arr)


# ex 2

# stack metodi bu metod default tarzda 2 ta yoki undan ortiq massivni uchinchi massivga har birini alohida qo'shadi
# mana bunaqa [[arr1], [arr2]]



# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2))

# print(arr)


# ex 3

# axis artibuti bu atribut bilan biz jadvallarning nechanchi elementlari olinishini berishimiz mumkin
# masalan [[1,4],[2,5],[3,6]] olinadi

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)

# ex 4

# hstack bu metod bilan biz haight bo'yicha qiymatlarni stack qila olamiz

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

# print(arr)


# ex 5

# vstack width uchun 

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


# ex 6 


# dstack balandlik bo'yicha olish uchun kerak

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)