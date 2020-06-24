file = open('kd.blocks.txt', 'r')

for line in file:
	print(f'"{line.strip()}",', end='')

print('')