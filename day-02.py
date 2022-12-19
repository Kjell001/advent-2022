map1 = {
	'A': {'X': 3+1, 'Y': 6+2, 'Z': 0+3},
	'B': {'X': 0+1, 'Y': 3+2, 'Z': 6+3},
	'C': {'X': 6+1, 'Y': 0+2, 'Z': 3+3}
}

map2 = {
	'A': {'X': 0+3, 'Y': 3+1, 'Z': 6+2},
	'B': {'X': 0+1, 'Y': 3+2, 'Z': 6+3},
	'C': {'X': 0+2, 'Y': 3+3, 'Z': 6+1}
}

total_score1 = 0
total_score2 = 0
with open('input-02.txt', 'r') as file:
	for line in file:
		p1, p2 = tuple(line.strip().split())
		total_score1 += map1[p1][p2]
		total_score2 += map2[p1][p2]

print('Answer 1:', total_score1)
print('Answer 2:', total_score2)

