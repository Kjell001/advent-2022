import re
import copy

def get_graph():
	graph = {}
	with open('input-16.txt', 'r') as file:
		for line in file:
			valves = re.findall(r'[A-Z]{2}', line)
			flow = int(re.search(r'\d+', line)[0])
			graph[valves[0]] = {
				'flow': flow,
				'tunnels': tuple(valves[1:])
			}
	return graph

def next_node(graph, chain, time_left):
	visited = set()
	check = set([chain[-1]])
	candidates = {}
	time = 0
	# Loop until exhausted or no more possible yield
	while check and time < time_left - 1:
		check_next = set()
		for key in check:
			visited.add(key)
			# Add possible candidates
			valve = graph[key]
			if key not in chain and valve['flow']:
				candidates[key] = {
					'cost': time + 1,
					'yield': (time_left - time - 1) * valve['flow']
				}
			# Expand check,ist for next iteration
			for tunnel in valve['tunnels']:
				if tunnel not in visited:
					check_next.add(tunnel)
		# Set up next iteration
		check = check_next
		time += 1
	return candidates

def optimal_path(graph, start, time):
	progress = [{
		'chain': [start],
		'total_yield': 0,
		'time_left': time
	}]
	best_path = None
	# BFS
	while progress:
		progress_next = []
		for path in progress:
			candidates = next_node(graph, path['chain'], path['time_left'])
			if candidates:
				# Branch paths
				for key, spec in candidates.items():
					progress_next.append({
						'chain': path['chain'] + [key],
						'total_yield': path['total_yield'] + spec['yield'],
						'time_left': path['time_left'] - spec['cost']
					})
			else:
				# Check if best
				if not best_path or path['total_yield'] > best_path['total_yield']:
					best_path = path
		progress = progress_next
	return best_path

cave = get_graph()

#[print(k,v) for k,v in next_node(cave, ['AA'], 30).items()]

[print(k, v) for k, v in optimal_path(cave, 'AA', 30).items()]

