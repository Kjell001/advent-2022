import re
import copy

with open('input-5.txt', 'r') as file:
	# Read stacks
	stacks = None
	for line in file:
		line = line.strip('\n')
		if not line:
			break
		crates = line[1::4]
		if not stacks:
			stacks = [[] for _ in range(len(crates))]
		for i, crate in enumerate(crates):
			stacks[i].append(crate)
	# Clean up stacks
	for i, stack in enumerate(stacks):
		stack.pop()
		stacks[i] = [x for x in stack[::-1] if x.strip()]
	# Process moves
	stacks2 = copy.deepcopy(stacks)
	for line in file:
		amount, src, dest = tuple(int(x) for x in re.findall(r'\d+', line))
		src -= 1
		dest -= 1
		# CrateMover 9000
		for _ in range(amount):
			stacks[dest].append(stacks[src].pop())
		# CrateMover 9001
		stacks2[dest][-amount:] += stacks2[src][-amount:]
		del stacks2[src][-amount:]

print('Answer 1:', ''.join(stack.pop() if stack else '' for stack in stacks))
print('Answer 2:', ''.join(stack.pop() if stack else '' for stack in stacks2))

