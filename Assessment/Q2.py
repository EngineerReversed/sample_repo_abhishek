from string import ascii_uppercase
k=0
for i in range(0, 6):
    for j in range(i+1):
      if j==i:
          print str(ascii_uppercase[k])
          k=k+1
      else:
          print str(ascii_uppercase[k]),
          k=k+1
