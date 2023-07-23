n,a,d = int(input()),100,100
for x in range(n):i = input().split();d,a = d-(int(i[0])*(int(i[0])>int(i[1]))),a-(int(i[1])*(int(i[0])<int(i[1])))
print(str(a)+'\n'+str(d))