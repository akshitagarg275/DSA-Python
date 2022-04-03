def toh(n,from_bar,to_bar,aux_bar):
    if n==1:
        print(f"Move disc 1 from {from_bar} to bar {to_bar}")
        return
    
    toh(n-1,from_bar,aux_bar,to_bar)
    print(f"Move disc {n} from {from_bar} to bar {to_bar}")
    toh(n-1,aux_bar,to_bar,from_bar)

n=3
toh(n,'A','C','B')