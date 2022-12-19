import re

# Method for comparing packets
def compare_packets(a, b):
	for p, q in zip(a, b):
		if type(p) is list or type(q) is list:
			result = compare_packets(
				p if type(p) is list else [p],
				q if type(q) is list else [q]
				)
			if result is not None:
				return result
			else:
				continue
		# Both are integers
		if   p < q:
			return True
		elif p > q:
			return False
	if len(a) != len(b):
		return len(a) < len(b)


# Convenience class for sorting
class Packet (object):
	def __init__(self, items):
		self.items = items
	
	def __lt__(self, other):
		return compare_packets(self.items, other.items)


# Read packet data
with open('input-13.txt', 'r') as file:
	raw = file.read()
code = '[' + re.sub(']\n', '],', raw) + ']'
packets = [Packet(x) for x in eval(code)]

# Get sum of indexes of ordered packets
index_sum = 0
for i, (a, b) in enumerate(zip(packets[::2], packets[1::2])):
	index_sum += i + 1 if a < b else 0

print('Answer 1:', index_sum)

# Sprt all packets
div1, div2 = Packet([[2]]), Packet([[6]])
packets.extend([div1, div2])
packets.sort()
print('Answer 2:', (packets.index(div1) + 1) * (packets.index(div2) + 1))

