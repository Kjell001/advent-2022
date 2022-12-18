
import console
import time

# Set up grid
BIG = 1e5
grid = {}
with open('input-12.txt', 'r') as file:
	for y, line in enumerate(file):
		for x, char in enumerate(line.strip()):
			if char == 'S':
				char = 'a'
				source = (x, y)
			if char == 'E':
				char = 'z'
				target = (x, y)
			grid[(x, y)] = {
				'dist': BIG,
				'height': ord(char),
				'candidate': False,
				'checked': False
				}
x_max = x
y_max = y
grid[source]['dist'] = 0
grid[source]['candidate'] = True

def print_grid():
	console.clear()
	for y in range(y_max + 1):
		for x in range(x_max + 1):
			coord = grid[(x, y)]
			col = (1.0, 1.0, 1.0)
			if   p == (x, y)       : col = (0.8, 0.0, 0.0)
			if   target == (x, y)  : col = (0.4, 0.4, 1.0)
			elif coord['checked']  : col = (0.5, 0.5, 0.5)
			elif coord['candidate']: col = (0.0, 0.8, 0.0)
			console.set_color(*col)
			print(chr(coord['height']), end = '')
		print()
	time.sleep(0.1)
	console.set_color(1, 1, 1)

# Search for path using Dijkstra's
deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
unchecked = lambda: (
	(k, v) for k, v in grid.items() if v['candidate'] and not v['checked']
	)
i = 0
p = True
while p:
	p, _ = min(unchecked(), key = lambda x: x[1]['dist'])
	if p == target:
		break
	coord = grid[p]
	coord['checked'] = True
	# Iterate over neighbours
	for dx, dy in deltas:
		q = (p[0] + dx, p[1] + dy)
		# Check if should be skipped
		if q not in grid:
			continue
		nb = grid[q]
		if nb['checked'] or coord['height'] + 1 < nb['height']:
			continue
		nb['candidate'] = True
		# Update distance
		if nb['dist'] > coord['dist'] + 1:
			nb['dist'] = coord['dist'] + 1
	# Print progress
	i += 1
	if not i % 100:
		print_grid()
print_grid()

print('Answer 1:', int(grid[target]['dist']))

