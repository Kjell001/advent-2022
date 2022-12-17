class P (object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def inf_norm(self):
		return max(abs(self.x), abs(self.y))
	
	def clamp(self):
		return P(max(-1, min(self.x, 1)), max(-1, min(self.y, 1)))
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __hash__(self):
		return hash((self.x, self.y))
	
	def __add__(self, other):
		return P(self.x + other.x, self.y + other.y)
	
	def __sub__(self, other):
		return P(self.x - other.x, self.y - other.y)
	
	def __repr__(self):
		return 'P({}, {})'.format(self.x, self.y)

vec = {
	'R': P( 1,  0),
	'U': P( 0,  1),
	'L': P(-1,  0),
	'D': P( 0, -1)
}

def trace_tail(amount):
	knots = [P(0, 0) for _ in range(amount)]
	trace = set()
	with open('input-9.txt', 'r') as file:
		for line in file:
			arg = line.strip().split()
			dir = arg[0]
			times = int(arg[1])
			for _ in range(times):
				move = vec[dir]
				for i in range(amount - 1):
					knots[i] += move
					diff = knots[i] - knots[i+1]
					if diff.inf_norm() > 1:
						move = diff.clamp()
					else:
						move = P(0, 0)
				knots[-1] += move
				trace.add(knots[-1])
	return trace

print('Answer 1:', len(trace_tail(2)))
print('Answer 2:', len(trace_tail(10)))

