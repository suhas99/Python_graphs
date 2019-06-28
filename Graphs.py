graph={
	'A':['A','B','C'],
	'B':['B'],
	'C':['B','D'],
	'D':['B']
}
print(graph,type(graph))


def create_edges(graph):
	edges=[]
	for node in graph:
		for neighbour in graph[node]:
			edges.append((node,neighbour))
	return edges

a=create_edges(graph)
print(a)


def find_path_betwwen_two_verticies(start,end,graph,path=[]):
	path=path+[start]

	if(start == end):
		return path
	#no start mentioned
	if not start in graph:
		return None
	for node in graph[start]:
		#node is not present in path list
		if node not in path:
			#recurssion
			newpath=find_path_betwwen_two_verticies(node,end,graph,path)
			if newpath:
				return newpath
	return None

b=find_path_betwwen_two_verticies('A','D',graph)
print(b)
