
import console
import time

SHOW_GRID = True
SHOW_STEP = 100
SHOW_WAIT = 0.2

DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))

# Set up grid
def read_grid():
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
					'checked': False
					}
	dim = (x + 1, y + 1)
	return grid, dim, source, target

# Show grid and path finding progress
def print_grid(grid, dim, start, current):
	if not SHOW_GRID:
		return
	console.clear()
	dim_x, dim_y = dim
	for y in range(dim_y):
		for x in range(dim_x):
			coord = grid[(x, y)]
			if   (x, y) == current : col = (0.8, 0.0, 0.0)
			elif (x, y) == start   : col = (0.0, 0.8, 0.0)
			elif coord['checked']  : col = (0.5, 0.5, 0.5)
			else                   : col = (1.0, 1.0, 1.0)
			console.set_color(*col)
			print(chr(coord['height']), end = '')
		print()
	time.sleep(SHOW_WAIT)
	console.set_color(1, 1, 1)

# Search for path using Dijkstra's
def find_path(grid, dim, start, func):
	unchecked = lambda: ((k, v) for k, v in grid.items() if not v['checked'])
	grid[start]['dist'] = 0
	i = 0
	p = start
	while p:
		# Assess stopping condition
		coord = grid[p]
		if func(p, coord):
			print_grid(grid, dim, start, p)
			return int(grid[p]['dist'])
		coord['checked'] = True
		# Iterate over neighbours
		for dx, dy in DELTAS:
			q = (p[0] + dx, p[1] + dy)
			# Check if should be skipped
			if q not in grid:
				continue
			nb = grid[q]
			if nb['checked'] or coord['height'] - 1 > nb['height']:
				continue
			# Update distance
			if nb['dist'] > coord['dist'] + 1:
				nb['dist'] = coord['dist'] + 1
		# Next coordinate
		p, _ = min(unchecked(), key = lambda x: x[1]['dist'])
		# Print progress
		i += 1
		if not i % SHOW_STEP:
			print_grid(grid, dim, start, p)

# Shortest path from target to source
grid, dim, source, target = read_grid()
success_1 = lambda x, y: x == source
print('Answer 1:', find_path(grid, dim, target, success_1))

# Shortest path from target to any 'a'
grid, dim, source, target = read_grid()
success_2 = lambda x, y: y['height'] == ord('a')
print('Answer 2:', find_path(grid, dim, target, success_2))

