import numpy as np


# ex 1 

# bu yerda where() metodiga 4 kiritilyabdi bu metodning qiymati arrayni ichidan 4 ga teng bo'lgan elementlarni qidiradi va bu 
# elementlarni indexsini qaytaradi

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

# ex 2

# bu kod massivning nechanchi elementlari juftligini ko'rsatadi

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)


# ex 3

# bu joyda searchsorted() metodi arrayni ichidan 7 ni qidiradi  va 7 ni indexsini qaytaradi faqatgina where() metodidan farqi bu metod
# tartiblangan massivlar uchun   va bu  metod binary Search algaritimida ishlaydi

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)


# ex 4

# bu joyda side atributi bilan qaysi tomondan qidirishini berib o'tamiz

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)