import matplotlib.pyplot as plt
import networkx as nx
import random
import math


cord_list = []
count = 0

with open('sample.tsp', 'r') as fh:
	for line in fh:
		if count > 7:
			cord_list.append(line.split())
		else:
			count += 1


del cord_list[-1]	

tuples_list = []

for item in cord_list:
    xVar = int(item[1])
    yVar = int(item[2])
    new_tuple = (xVar, yVar)
    tuples_list.append(new_tuple)

def get_distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance

totalDistance = 0

G = nx.Graph()

startPoint = tuples_list[0]

G.add_node(startPoint, pos = (float(startPoint[0]), float(startPoint[1])))
oldPoint = startPoint

while(len(tuples_list) > 0):
    rand_gen = random.randint(0,(len(tuples_list) - 1))
    
    xCord1 = startPoint[0]
    yCord1 = startPoint[1]
    
    nextPoint = tuples_list[rand_gen]
    
    xCord2 = nextPoint[0]
    yCord2 = nextPoint[1]
    
    pointDistance = get_distance(xCord1, yCord1, xCord2, yCord2)
    
    del tuples_list[0]
    
    totalDistance = pointDistance + totalDistance
    
    G.add_node(nextPoint, pos = (float(nextPoint[0]), float(nextPoint[1])))
    G.add_edge(oldPoint, nextPoint)
    oldPoint = nextPoint
    
    #G.add_node(startPoint)


#Graphing    
G.add_node(startPoint)
print totalDistance
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos = pos, with_labels = False, edge_color='black', node_color='blue', node_size=100)
plt.show()