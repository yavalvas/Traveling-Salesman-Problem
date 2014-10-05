import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import operator

# Distance formula function
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# Function that takes list as a paramater and calculates distance
def list_distance(list_a):
    alter_list = list_a
    first_tuple = alter_list[0]
    del alter_list[0]
    total_dist = 0
    while alter_list:
        next_tuple = alter_list.pop()
        dist = distance(first_tuple, next_tuple)
        total_dist = total_dist + dist
        first_tuple = next_tuple
    return total_dist

cord_list = []
count = 0

# Start reading file from 8th line
with open('sample.tsp', 'r') as fh:
	for line in fh:
		if count > 7:
			cord_list.append(line.split())
		else:
			count += 1

# Delete last line
del cord_list[-1]	

# Create a list of lists and load it with custom data
cities_list = []

for item in cord_list:
    city_name = int(item[0])
    xVar = float(item[1])
    yVar = float(item[2])
    cities_list.append([xVar, yVar, city_name])


unselected_cities = list(cities_list)
selected_cities = []

# Select 3 random cities
c_count = 0
for city in unselected_cities:
    if c_count < 3:
        rand_gen = random.randint(0, len(unselected_cities) - 1)
        selected_cities.append(unselected_cities[rand_gen])
        del unselected_cities[rand_gen]
        c_count += 1
    else:
        pass
 
# Initialize the graph
G = nx.Graph()

# Graph first 3 points
old_point = tuple(selected_cities[0])

for selcity in selected_cities:
    start_point = tuple(selcity)
    G.add_node(start_point, pos = (float(start_point[0]), float(start_point[1])))
    G.add_edge(old_point, start_point)
    old_point = start_point

# Loop, insert new point into the traveled cities
# where total distance is minimized
while len(unselected_cities) > 0:
    first_cord = unselected_cities[0]
    del unselected_cities[0]
    max_distance = 1000000000
    index = 0
    temp_list = selected_cities
    for i in range(len(selected_cities)):
        temp_list.insert(i, first_cord)
        copy_list = [j for j in temp_list]
        calc_distance = list_distance(copy_list)
        temp_list.pop(i)
        if calc_distance < max_distance:
            index = i
            max_distance = calc_distance

    selected_cities.insert(index, first_cord)
    
    next_point = (first_cord[0], first_cord[1])
    G.add_node(next_point, pos = (float(next_point[0]), float(next_point[1])))
    G.add_edge(old_point, next_point)
    old_point = next_point

print "Total Cities Traveled: ", len(selected_cities)

# Calculate the total distance
counter = 0
next_tuple = [0,0]
total_distance = 0

for city in selected_cities:
    print city
    first_tuple = city
    if counter == 0:
        dist = distance(first_tuple, next_tuple)
        next_tuple = first_tuple
        total_distance += dist
        counter += 1
    else:
        dist = distance(first_tuple, next_tuple)
        next_tuple = first_tuple
        total_distance += dist


final_distance = list_distance(selected_cities)

print "Total Distance: ", final_distance


pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos = pos, with_labels = False, edge_color='black', node_color='blue', node_size=100)
plt.title("Traveling Salesman - Insertion Heuristics")
plt.show()
