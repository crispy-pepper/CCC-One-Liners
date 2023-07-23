r,c,n = int(input()),int(input()),int(input())
g,d=[[0 for x in range(c)] for y in range(r)],{'R '+str(e):[] for e in range(1,r+1)}
d.update({'C '+str(h):[] for h in range(1,c+1)})

[d[input()].append(1) for x in range(n)]
fflip = lambda l:[(not x)+0 for x in l]
flip = lambda g,n,c,r:[fflip(g[e]) if e==n else g[e] for e in range(r)]
cflip = lambda g,n,c,r:[[(not g[e][n])+0 if i == n else g[e][i] for i in range(c)] for e in range(r)]
d=dict(filter(lambda k:d[k[0]]!=[],d.items()))
#print(d)
for (k,v) in d.items():
    g = flip(g,int(k[1:])-1,c,r) if k[0]=='R' and len(v)%2==1 else (cflip(g,int(k[1:])-1,c,r) if len(v)%2==1 else g)
    """if sum(v)%2==1:
        if k[0]=='R':
            g = flip(g,int(k[1:])-1,c,r)
            print('r')
        else:
            g = cflip(g,int(k[1:])-1,c,r)
            print('c')
    else:
        g = g
        print('np')
    print(k,v)
    print(*g,sep='\n')
    print()"""

print(sum(sum(g,[])))