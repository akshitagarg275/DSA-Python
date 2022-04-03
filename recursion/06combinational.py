def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def combination(n,r):
    return((fact(n))/(fact(n-r)*fact(r)))

print(int(combination(5,3)))