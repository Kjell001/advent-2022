import re

ROUNDS = 20
UNWORRY = 3


class Monkey (object):
	def __init__(self, specs):
		self.items = [int(s) for s in specs[0].split(', ')]
		# Make function
		self.operator = specs[1]
		self.operand = None if specs[2] == 'old' else int(specs[2])
		self.div = int(specs[3])
		self.move = {True: int(specs[4]), False: int(specs[5])}
		self.inspections = 0
	
	def receive(self, item):
		self.items.append(item)
	
	def handle(self, pack):
		for item in self.items:
			value = self.operand if self.operand else item
			item = item * value if self.operator == '*' else item + value
			item //= UNWORRY
			other = self.move[item % self.div == 0]
			pack[other].receive(item)
			self.inspections += 1
		self.items = []
	
	def __repr__(self):
		return 'Monkey: #{} {}'.format(self.inspections, self.items)


with open('input-11.txt', 'r') as file:
	all_specs = file.read()

specs_iter = re.finditer(r'items: ((?:\d+(?:, )?)*).*?= old (.) (\d+|old).*?by (\d+).*?monkey (\d+).*?monkey (\d+)', all_specs, flags = re.S)
monkeys = [Monkey(m.groups()) for m in specs_iter]
for round in range(ROUNDS):
	#print('Round', round)
	for i, m in enumerate(monkeys):
		m.handle(monkeys)
	#[print(i, m) for i, m in enumerate(monkeys)]

inspections_sorted = [m.inspections for m in sorted(monkeys, key = lambda x: -x.inspections)]
print('Answer 1:', inspections_sorted[0] * inspections_sorted[1])
	

