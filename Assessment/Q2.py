from string import ascii_uppercase
k=1
for i in range(1, 6):
    k=k+i
    print(" ".join(ascii_uppercase[i:k]))
