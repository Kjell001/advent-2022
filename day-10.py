CHECK_FIRST = 20
CHECK_STEP = 40
CHECK_LIMIT = 220
WIDTH = 40

cycle_count = 0
value = 1
total = 0
check = CHECK_FIRST
values = []
with open('input-10.txt', 'r') as file:
	for line in file:
		arg = line.strip().split()
		cycles = 2 if arg[0] == 'addx' else 1
		values += [value] * cycles
		cycle_count += cycles
		if cycle_count >= check:
			total += check * value
			check += CHECK_STEP
		if arg[0] == 'addx':
			value += int(arg[1])

print('Answer 1:', total)

pixels = ''
for i, v in enumerate(values):
	pos = i % WIDTH
	pixels += '#' if pos - 1 <= v <= pos + 1 else '.'
display = '\n'.join(pixels[i:i+WIDTH] for i in range(0, len(pixels), WIDTH))
print('Answer 2:')
print(display)

