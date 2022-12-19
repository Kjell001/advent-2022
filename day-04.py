import re

contain_count = 0
overlap_count = 0
with open('input-04.txt', 'r') as file:
	for line in file:
		spec = [int(s) for s in re.findall(r'\d+', line.strip())]
		if (spec[0] >= spec[2] and spec[1] <= spec[3]) or (spec[0] <= spec[2] and spec[1] >= spec[3]):
			contain_count += 1
		if spec[2] <= spec[1] <= spec[3] or spec[0] <= spec[3] <= spec[1]:
			overlap_count += 1

print('Answer 1:', contain_count)
print('Answer 2:', overlap_count)

