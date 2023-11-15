import numpy as np


                                        # Filtering arrays - Massivlarni Filtirlash

# massivlarni filtirlash deb mavjud massivdan kerakli elementlarni olish va yangi massiv yaratishga aytiladi



# ex 1

# bu  masalada arr massivi va x massivi berilgan yangi massivga arr massiving 0 chi va 2 indexsidagi qiymatlar saqlanyabdi
# biz buni saqlanishini x massivinig mantiqit qiymatlari orqali bermoqdamiz yani 0 chi elementini  olinishi True 
# 2 chi elementini olinishi False

# arr = np.array([41, 42, 43, 44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)



# ex 2


# bu joyda massivning elementi 42 dan katta bo'lsa yangi massivga qo'shilyabdi

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)



# ex 3

# bu misolda massivning juft elementlari olinmoqda


arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# ex 4

# bu misolda massivning juft elementlari olinmoqda

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)