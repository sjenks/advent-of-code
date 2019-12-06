import networkx

def parse():
	filepath = "input.txt"

	edges = []
	with open(filepath) as fp:
		for count, line in enumerate(fp):
			edges.append(line.strip().split(")"))
	return edges

def main():
	edges = parse()
	graph = networkx.DiGraph()

	for e in edges: 
		graph.add_edge(e[0], e[1])

	print(networkx.transitive_closure(graph).size())

	undirected = graph.to_undirected()
	length = networkx.shortest_path_length(undirected, "YOU", "SAN")
	length -= 2 # not counting you and santa
	print("you-to-santa", length)

if __name__ == "__main__":
	main()