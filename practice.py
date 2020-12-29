a = [1, 2, 3]
b = [1 for x in a]
ab = []
for i in range(len(a)):
    ab.append(a[i]-b[i])
print(ab)