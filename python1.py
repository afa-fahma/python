n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()    


n=int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end= " ")
    print()    


n=int(input("Enter the number of rows: "))
for i in range (1, n+1):
    for j in range (n-i):
        print(" ", end= " ")
    for k in range(i):
        print("*", end= " ")
    print()       

 
n=int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end= " ")

    for k in range(i):
        print("*", end=" ")   
    print()    


n=int(input("Enter the number of rows: ")) 
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end= " ")
    print()    


n=int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end= " ")
    print()        


n=int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()        


n=int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range ( 2 * i - 1):
        print("*", end= " ")
    print()
for i in  range(n-1, 0 , -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range( 2 * i - 1):
        print("*", end =" ")
    print()          