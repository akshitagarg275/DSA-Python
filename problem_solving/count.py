s=input()
freq={}

# for i in s:
#     if freq.get(i) is None:
#         freq[i]=1
#     else:
#         freq[i]+=1

for i in s:
    if freq.get(i.lower()) is None:
        freq[i.lower()]=1
    else:
        freq[i.lower()]+=1

print(freq)