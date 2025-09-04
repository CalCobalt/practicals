for i in range(1, 21, 2): 
    print(i, end=' ') 
print()

#a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
star = int(input("Enter number of stars: "))
print("Number of stars:", star, end=' ')
for i in range(star):
    print('*', end='')
print()

#d
line = int(input("Enter number of lines of increasing stars: "))
for i in range(1, line + 1):
    for j in range(i):
        print('*', end='')
    print()
print()