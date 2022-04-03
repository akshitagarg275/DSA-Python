def fib(n):
    if n<0:
        print("Invalid num")
    elif n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# print(fib(3))
sum=0
for i in range(6):
    # print(fib(i))
    sum+=fib(i)
    last=fib(i)
print("sum is ",sum)
print("last is ",last)