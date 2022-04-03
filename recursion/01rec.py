def func(n):
    if n>0:
        func(n-1)
        func(n-1)
        print(n,end=",")

func(3)