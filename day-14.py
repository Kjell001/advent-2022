import re
import copy
import console

def load_cave():
	columns = {}
	limit_y = 0
	with open('input-14.txt', 'r') as file:
		for line in file:
			coords = [(int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', line)]
			for i in range(len(coords) - 1):
				x1, y1, x2, y2 = *coords[i], *coords[i+1]
				if x1 == x2:
					for y in range(min(y1, y2), max(y1, y2) + 1):
						columns.setdefault(x1, set()).add(y)
				else:
					for x in range(min(x1, x2), max(x1, x2) + 1):
						columns.setdefault(x, set()).add(y1)
				limit_y = max(limit_y, y1, y2)
		return columns, limit_y

LANDED  = 0
BLOCKED = 1
ABYSS   = 2
SLIDE = ((-1,  1), ( 1,  1))
def drop_grain(columns, src_x, src_y, floor_y = None):
	if src_y in columns.get(src_x, []):
		return BLOCKED
	dst_y = min((y for y in columns.get(src_x, []) if y >= src_y), default = None)
	if not dst_y:
		if not floor_y:
			# Into the abyss
			return ABYSS
		else:
			# Use the floors, Luke
			columns.setdefault(src_x, set()).add(floor_y - 1)
			return LANDED
	else:
		dst_y -= 1
	# Check if it can slide
	for dx, dy in SLIDE:
		result = drop_grain(columns, src_x + dx, dst_y + dy, floor_y)
		if result == BLOCKED:
			continue
		else:
			return result
	columns[src_x].add(dst_y)
	return LANDED

def print_columns(cave, sand, floor_y):
	null = []
	for y in range(floor_y + 1):
		line = []
		for x in range(min(cave), max(cave) + 1):
			if x not in cave : c = (0.3, 0.3, 0.3)
			elif y in cave[x]: c = (1.0, 1.0, 1.0)
			elif y in sand[x]: c = (0.8, 0.7, 0.0)
			else             : c = (0.3, 0.3, 0.3)
			console.set_color(*c)
			print('0', end = '')
		print()
	console.set_color(1, 1, 1)

# Set up cave
cave, y_max = load_cave()

# Pour until abyssing
sand = copy.deepcopy(cave)
grains = 0
while drop_grain(sand, 500, 0) == LANDED:
	grains += 1
print_columns(cave, sand, y_max)
print('Answer 1:', grains)

# Pour until flooded
sand = copy.deepcopy(cave)
grains = 0
while drop_grain(sand, 500, 0, y_max + 2) == LANDED:
	grains += 1
print_columns(cave, sand, y_max)
print('Answer 2:', grains)


