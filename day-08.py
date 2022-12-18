with open('input-8.txt', 'r') as file:
	raw = file.readlines()
forest = [[int(i) for i in row.strip()] for row in raw]

SIZE = len(forest)
visible = set()

# Check all rows and columns from both ends
for i in range(SIZE):
	col = [row[i] for row in forest]
	row = forest[i]
	cap = [-1] * 4
	for j in range(SIZE):
		# North
		index = j
		if col[index] > cap[0]:
			visible.add(SIZE * i + index)
		cap[0] = max(cap[0], col[index])
		# West
		if row[index] > cap[1]:
			visible.add(SIZE * index + i)
		cap[1] = max(cap[1], row[index])
		# South
		index = SIZE - j - 1
		if col[index] > cap[2]:
			visible.add(SIZE * i + index)
		cap[2] = max(cap[2], col[index])
		# East
		if row[index] > cap[3]:
			visible.add(SIZE * index + i)
		cap[3] = max(cap[3], row[index])

print('Answer 1:', len(visible))

score_max = 0
# Check each coordinate in for directions
for x in range(1, SIZE - 1):
	col = [row[x] for row in forest]
	for y in range(1, SIZE - 1):
		row = forest[y]
		hut = forest[y][x]
		dirs = [
			col[y - 1::-1],
			row[x + 1:],
			col[y + 1:],
			row[x - 1::-1]
			]
		score = 1
		for dir in dirs:
			score *= next((i + 1 for i, t in enumerate(dir) if t >= hut), len(dir))
		score_max = max(score_max, score)

print('Answer 2:', score_max)

