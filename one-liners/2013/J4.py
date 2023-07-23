mins,l,m,c = int(input()),sorted([int(input()) for x in range(int(input()))]),0,0
while not(len(l) <= 0 or mins-l[0] < 0):c,mins=c+1,mins-l[0];del l[0]
print(c)

