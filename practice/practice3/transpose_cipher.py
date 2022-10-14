# Пользователь вводит пароль. Примените к паролю шифр транспонирования и сохраните результат в файл.
import numpy as np

password = input()
pas = np.array([ord(ch) for ch in password])


encoding = [el for el in pas]
if len(encoding) % 4 != 0:
    n = 4 - len(encoding) % 4

    encoding.extend([-1] * n)

pas = np.array(encoding).reshape((4, -1))
decoded = ''
for j in range(pas.shape[1]):
    for i in range(pas.shape[0]):
        if pas[i, j] == -1:
            break
        decoded += str(chr(pas[i, j]))


with open('transpose_cipher.txt','w') as ouf:
    ouf.write(decoded)