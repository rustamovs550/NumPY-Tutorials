import numpy as np


# ex 1

# 1D massiv iteratsiya qilish

# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)



# ex 2


# 2d massivlarni iteratsiya qilish

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)


#  ex 3 

# 3d massivni iteratsiya qilish

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)


# ex 4

# nditer() metodi yordamida biz arr nomli 3d arrayni bir nechta for qilmasdan bitta for siklini o'zida olmoqdamiz 


# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)



# ex 5

# biz iteratsiya paytida elementlarni malumot turini  o'zgartirish uchun op_dtypes argumentidan foydalanamiz va unga 
# kutilgan malumotlar turini berishimiz kerak
# 
# NumPy o'z joyidagi elementlarning malumotlar turini o'zgartirmaydi shuning uchun bu amalni bajarish uchun boshqa bo'sh joy kerak
# bu qo'shimcha joy bufer deb ataladi va biz ui nditerda yoqish uchun flags=['buffered'] deb berishimiz kerak 

# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)




# ex 6


# har bir iteratsiya paytida bizga elementning turgan joyi kerak bo'lib qolishi mumkin ndenumerate() metodi bizga har bir arrayning
# turgan o'rni haqida ham malumot beradi

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)