with open('input-06.txt', 'r') as file:
	stream = file.readline()

N1 = 4
N2 = 14
for i in range(len(stream)):
	if N1 and len(set(stream[i:i + N1])) == N1:
		print('Answer 1:', i + N1)
		N1 = None
	if len(set(stream[i:i + N2])) == N2:
		print('Answer 2:', i + N2)
		break

