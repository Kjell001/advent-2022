import re
import cProfile


class Monkey (object):
	def __init__(self, specs):
		self.items = [int(s) for s in specs[0].split(', ')]
		self.operator, self.operand = specs[1], specs[2]
		self.div = int(specs[3])
		self.move = {True: int(specs[4]), False: int(specs[5])}
		self.inspections = 0
	
	def receive(self, item):
		self.items.append(item)
		
	def handle(self, pack, unworry, pack_factor):
		for item in self.items:
			# Inspect item
			value = item if self.operand == 'old' else int(self.operand)
			item = item * value if self.operator == '*' else item + value
			# Reduce item value
			if not unworry:
				item %= pack_factor
			else:
				item //= unworry
			# Hand to other monkey
			other = self.move[item % self.div == 0]
			pack[other].receive(item)
			self.inspections += 1
		self.items = []


# Store monkey specifications and initial state
def get_pack():
	with open('input-11.txt', 'r') as file:
		all_specs = file.read()
	specs_iter = re.finditer(r'items: ((?:\d+(?:, )?)*).*?= old (.) (\d+|old).*?by (\d+).*?monkey (\d+).*?monkey (\d+)', all_specs, flags = re.S)
	return [Monkey(m.groups()) for m in specs_iter]

def do_rounds(pack, rounds, unworry):
	# Determine product of monkey divs
	pack_factor = 1
	for m in pack:
		pack_factor *= m.div
	# Inspect and move items
	for round in range(rounds):
		for i, m in enumerate(pack):
			m.handle(pack, unworry, pack_factor)
	# Product of top 2
	pack.sort(key = lambda x: -x.inspections)
	return pack[0].inspections * pack[1].inspections

print('Answer 1:', do_rounds(get_pack(), 20, 3))
print('Answer 2:', do_rounds(get_pack(), 10000, False))
	

