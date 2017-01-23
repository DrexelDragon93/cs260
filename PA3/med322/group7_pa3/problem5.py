#!/usr/bin/env python

def dijkstra(a, start):
	dist = {}
	pred = {}
	dist[start] = 0
	pred[start] = None
	unvis = []
	
	#Initializing distances from the starting vertex
	for v, d in a[start].items():
		dist[v] = d
	#Marking nodes as unvisited	
	for v in a:
		if v != start:
			unvis.extend(v)
	#Finding minimum distances
	for v in a:
		if v != start:
			for w in a[v]:
				newDist = dist[v] + a[v][w]
				if newDist < dist[w]:
					dist[w] = newDist
					unvis.remove(w)
					pred[w] = v
	return(dist, pred)
		
	
sixGraph = {'1' : {'2':4, '3':1, '4':5, '5':8, '6':10},
	    '2' : {},
	    '3' : {'2':2},
	    '4' : {'5':2},
	    '5' : {'6':1},
	    '6' : {}} 

print(dijkstra(sixGraph,'1'))
