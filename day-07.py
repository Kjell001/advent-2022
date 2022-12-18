# Build file tree
tree = {'parent': None, 'dirs': {}, 'files': []}
with open('input-7.txt', 'r') as file:
	for line in file:
		arg = line.strip().split()
		if   arg[1] == 'ls':
			continue
		elif arg[1] == 'cd':
			if   arg[2] == '..':
				# Go up
				current_dir = current_dir['parent']
			elif arg[2] == '/':
				# Go to root
				current_dir = tree
			else:
				# Go to directory
				current_dir = current_dir['dirs'][arg[2]]
		elif arg[0] == 'dir':
			# Add dir
			current_dir['dirs'][arg[1]] = {
					'parent': current_dir,
					'dirs': {},
					'files': []
					}
		else:
			# Add file
			current_dir['files'].append(int(arg[0]))

def dir_print(dir, depth = 0):
	if depth == 0:
		print('/')
	for k, v in dir['dirs'].items():
		print('. ' * (depth - 1) + '└ ' + k)
		dir_print(v, depth + 1)
	for f in dir['files']:
		print('. ' * depth + str(f))

def dir_size(dir, rsizes):
	size = sum(dir['files'])
	for k, v in dir['dirs'].items():
		size += dir_size(v, rsizes)
	rsizes.append(size)
	return size

# dir_print(tree)

THRESHOLD = 100e3
TOTAL = 70e6
FREE = 30e6
sizes = []
used = dir_size(tree, sizes)

print('Answer 1:', sum(s for s in sizes if s <= THRESHOLD))
print('Answer 2:', min(s for s in sizes if s >= FREE - (TOTAL - used)))

