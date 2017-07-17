filename = 'shakya.txt'
with open(filename) as f_obj:
    lines = f_obj.readlines()
print(len(lines))
