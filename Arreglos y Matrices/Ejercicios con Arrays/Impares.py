array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
impar = 0
for i in range(len(array)):
    if array[i] % 2 != 0:
        print(f"{array[i]} es impar")
        impar += array[i]

print(impar)