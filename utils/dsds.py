

m = [[1,2],[2,2]]

for i in range(len(m)):
	for x in range(len(m[i])):
		m[i][x] = (i, x)

print(m)

