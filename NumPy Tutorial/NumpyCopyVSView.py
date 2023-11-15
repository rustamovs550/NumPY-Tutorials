import numpy as np

# ex 1

# bu yerda arr massivdan nusxa olinib x massivga saqlanmoqda va arr massivning 0 chi elementi 42 ga tenglanyabdi lekin x massivga buni hech qanday tasiri bolmaydi

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)



# ex 2

# bu misolda biz view dan foydalanganimiz uchun har qanday qilingan o'zgarishning x massivga ham tasiri mavjud



# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)



# ex 3

# bu misolda base atributi bilan biz yangi massiv o'zining bazasiga egami yoki ega emasligi haqida malumot olishimiz mumkin

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
