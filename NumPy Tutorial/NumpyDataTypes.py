import numpy as np


# ex 1

# bu misolda bizga numpy hosila qilagan array qanaqa malumotlar turidaligini chiqarib beradi
# int64 chiqadi

# arr = np.array([1, 2, 3, 4])

# print(arr.dtype)


# ex 2

# biz bu misolda arrayni yaratish jarayonida qanaqa turdagi malumotlar bo'lishini birdaniga berib yuboryabmiz

# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)


# ex 3

# biz bu joyda arrayni i4 yani ahr bir integer 4 bayt bo'lishini belgilayabmiz

# arr = np.array([1, 2, 3, 4], dtype='i4')

# print(arr)
# print(arr.dtype)


# ex 4

# bu joyda arr nomli massiv elementlari float tipida ochilyabdi  astype() funksiyasi bilan biz bu float sonlarni integer tipiga aylantirib yangi newarr nomli o'zgaruvchiga saqlayabmiz

# arr = np.array([1.1, 2.1, 3.1])

# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)


# ex 5


# bu joyda biz int ni bool ga aylantiryabmiz

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)