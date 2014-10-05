import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import operator


cord_list = []
count = 0

with open('sample.tsp', 'r') as fh:
	for line in fh:
		if count > 7:
			cord_list.append(line.split())
		else:
			count += 1

del cord_list[-1]	

cities_list = []

for item in cord_list:
    city_name = int(item[0])
    xVar = int(item[1])
    yVar = int(item[2])
    cities_list.append([xVar, yVar, city_name])

def get_distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance

startPoint = tuple(cities_list[0])
del cities_list[0]

oldPoint = startPoint
 
G = nx.Graph()
G.add_node(startPoint, pos = (float(startPoint[0]), float(startPoint[1])))

totalDistance = 0

distance_dict = {}

for city in cities_list:
    distance = get_distance(startPoint[0], city[0], startPoint[1], city[1])
    totalDistance += distance
    distance_dict[city[2]] = distance
    # returns list of tuples with city number and distance to the city
    sorted_distance = sorted(distance_dict.iteritems(), key = operator.itemgetter(1), reverse = False)
    shortest_tuple = sorted_distance[0]
    del sorted_distance[0]
    if city[2] == shortest_tuple[1]:
        del cities_list[0]
    
    nextPoint = (city[0], city[1])
    G.add_node(nextPoint, pos = (float(nextPoint[0]), float(nextPoint[1])))
    G.add_edge(oldPoint, nextPoint)
    oldPoint = nextPoint

print totalDistance
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos = pos, with_labels = False, edge_color='black', node_color='blue', node_size=100)
plt.show()
