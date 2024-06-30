import random

n = random.randint(3, 20)
password = []

for i in range(1, n):
        
    for j in range(i + 1, n):
            
        if n % (i + j) == 0:
            password.append(i)
            password.append(j)

print(f"Выпало {n}, ваш пароль: {password}")
