#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):

    first=0
    second=1

  
    for i in range(1,n+1):
        first,second=second,first+second
    return first 
print fibonacci(6)
print fibonacci(36)
#>>> 14930352
