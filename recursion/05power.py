def pow(b,p):
    if p==0: 
        return 1

    return b*pow(b,p-1)

print(pow(2,3))