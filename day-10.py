CHECK_FIRST = 20
CHECK_STEP = 40
CHECK_LIMIT = 220

cycle_count = 0
value = 1
total = 0
check = CHECK_FIRST
with open('input-10-ex.txt', 'r') as file:
	for line in file:
		arg = line.strip().split()
		cycle_count += 2 if arg[0] == 'addx' else 1
		if cycle_count >= check:
			total += check * value
			check += CHECK_STEP
			if check > CHECK_LIMIT:
				break
		if arg[0] == 'addx':
			value += int(arg[1])
		print(cycle_count, value)

print('Answer 1:', total)

