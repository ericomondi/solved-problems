# provide a code that will read an integer,n, from input.

# Without using any string methods, try to print the following:
# if n = 5
# print 12345

def print_n():
    n = int(input())
    for i in range(1,n + 1):
        print (i, end = "")