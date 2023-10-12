n = int(input())
A = []
s = input().split()
error = False
B = []
for i in range(n):
    d = int(s[i])
    if abs(d) > 10000:
        error = True
    else:
        A.append(d)
if not error:
    for a in A:
        if a not in B:
            B.append(a)
print(len(B))
