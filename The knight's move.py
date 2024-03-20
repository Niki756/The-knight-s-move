n = []
n.extend(input())
desk = [['.']*8 for _ in range(8)]
col = 'abcdefgh'
row = '87654321'
x = int(col.find(n[0]))
y = int(row.find(n[1]))
desk[y][x] = 'N'

for i in range(8):
    for j in range(8):
        if ((y+1)-(i+1))*((x+1)-(j+1))==2 or ((y+1)-(i+1))*((x+1)-(j+1))==-2:
            desk[i][j]='*'
            
for i in desk:
    print(*i)