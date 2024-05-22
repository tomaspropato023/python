#EJ Multiplos

for i in range (1, 101):
    if (i % 2 == 0) and (i % 3 == 0):
        print(f"{i} es multiplo de 2 y 3.")
    elif (i % 2 == 0):
        print(f"{i} es multiplo de 2.")
    elif (i % 3 == 0):
        print(f"{i} es multiplo de 3.")
    