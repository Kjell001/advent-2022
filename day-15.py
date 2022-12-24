import re

class P (object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __add__(self, other):
		return P(self.x + other.x, self.y + other.y)
	
	def __sub__(self, other):
		return P(self.x - other.x, self.y - other.y)
	
	def __mod__(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)
	
	def __mul__(self, other):
		return P(other * self.x, other * self.y)
	
	def __repr__(self):
		return 'P({}, {})'.format(self.x, self.y)

sensors = []
beacons = []
mdist = []

with open('input-15.txt', 'r') as file:
	for line in file:
		coords = [P(int(x), int(y)) for x, y in re.findall(r'(-?\d+), y=(-?\d+)', line)]
		sensors.append(coords[0])
		beacons.append(coords[1])
		mdist.append(coords[0] % coords[1])

def count_empty(ref_y):
	row = set()
	for s, dm in zip(sensors, mdist):
		dy = abs(s.y - ref_y) 
		xmin, xmax = s.x - dm + dy, s.x + dm - dy
		row |= set(range(xmin, xmax + 1))
	row -= set(p.x for p in beacons if p.y == ref_y)
	return len(row)

# Traverse perimeter of every sensor, since missing beacon must be on perimeter
START = (P( 1,  0), P( 0, -1), P(-1,  0), P( 0,  1))
DELTA = (P(-1, -1), P(-1,  1), P( 1,  1), P( 1, -1))
def find_beacon(dim_max, freq):
	for s, dm in zip(sensors, mdist):
		# Traverse four perimeter sides
		for coord, delta in zip(START, DELTA):
			coord *= (dm + 1)
			coord += s
			for _ in range(dm + 1):
				# Check if out of bounds
				if not 0 <= coord.x <= dim_max or not 0 <= coord.y <= dim_max:
					continue
				# Check if coord is in other's range
				for s_other, dm_other in zip(sensors, mdist):
					if coord % s_other <= dm_other:
						break
				else:
					return coord.x * freq + coord.y
				# Set up for next iteration
				coord += delta


PROBE_Y = 10
FREQ = 4000000
DIM_MAX = 20

PROBE_Y = 2000000
DIM_MAX = 4000000



print('Answer 1:', count_empty(PROBE_Y))
print('Answer 2:', find_beacon(DIM_MAX, FREQ))

