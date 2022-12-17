total_calories = [0,]
with open('input-1.txt', 'r') as file:
	for line in file:
		if line.strip():
			total_calories[-1] += int(line)
		else:
			total_calories.append(0)

print('Answer 1:', max(total_calories))
total_calories.sort(reverse = True)
print('Answer 2:', sum(total_calories[:3]))

