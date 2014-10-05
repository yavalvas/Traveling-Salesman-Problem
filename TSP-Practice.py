import sys
import math

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def listDistance(alist):
	alteringList = alist
	firstTuple = alteringList[0]
	del alteringList[0]
	total_dist = 0
	while alteringList:
		nextTuple = alteringList.pop()
		dist = distance(firstTuple, nextTuple)
		total_dist = total_dist + dist
		firstTuple = nextTuple
	return total_dist


def main():
	list_of_coordinates = [(80,90), (12,22), (14,15), (18, 30), (1000, 1000)]
	insert_coord = (44,81)
	testlist = list_of_coordinates
	large_distance = 100000000000000
	for i in range(len(list_of_coordinates)):
		print i
		testlist.insert(i, insert_coord)
		print testlist
		copylist = [j for j in testlist]
		calc_distance = listDistance(copylist)
		print calc_distance
		testlist.pop(i)
		print testlist
		if calc_distance < large_distance:
			chosen_index = i
			print "Chosen Index ", chosen_index
			large_distance = calc_distance
	list_of_coordinates.insert(chosen_index, insert_coord)

	print "Test List", list_of_coordinates
	print chosen_index
	print large_distance
	#sometotal = listDistance(list_of_coordinates)
	#print sometotal

main()

