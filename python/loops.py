# provide a code that reads an integer, n, 
# from input. 
# For all non-negative integers i < n , print i**2

n = int(input())
for i in range(0,n):
    if i > -1:
        print(i**2)
    else:
        pass