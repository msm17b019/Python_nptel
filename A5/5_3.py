numbers=input().split()
k=int(input())
q=[]
for y in numbers:
    q.append(int(y))
maximum=sorted(q, reverse=True)
minimum=(sorted(q))
maxi=[]
mini=[]
for m in maximum:
    if m not in maxi:
        maxi.append(m)
for z in minimum:
    if z not in mini:
        mini.append(z)
print(maxi[k-1]+mini[k-1],end="")