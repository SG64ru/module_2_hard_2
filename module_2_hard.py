vstavka = int(input("Введите число от 3 до 20 " ))
password = ""
for i in range(1, vstavka):
    for j in range(i, 21):

        if i + j > vstavka:
            break
        if vstavka % (i + j) == 0 and i != j:

            password += str(i)
            password += str(j)
print(password)




