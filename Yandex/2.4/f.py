n = int(input())
nod = 0

for i in range(n):
    x = int(input())
    if nod == 0:
        nod = x
    else:
        while nod != x:
            if nod > x:
                nod = nod - x
            else:
                x = x - nod
        nod = x

print(nod)
