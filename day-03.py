
total_priority = 0
total_badge = 0
badge = []

def get_priority(item):
	ascii = ord(item)
	return ascii + (-96 if ascii > 96 else -64 + 26)

with open('input-03.txt', 'r') as file:
	for i, line in enumerate(file):
		items = line.strip()
		comp1, comp2 = line[:len(items) // 2], line[len(items) // 2:]
		for item in comp1:
			if item in comp2:
				total_priority += get_priority(item)
				break
		if i % 3 == 0:
			badge = {*items}
		else:
			badge &= {*items}
		if i % 3 == 2:
			total_badge += get_priority(*badge)

print('Answer 1:', total_priority)
print('Answer 2:', total_badge)

