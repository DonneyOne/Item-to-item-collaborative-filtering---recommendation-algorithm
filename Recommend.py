import numpy as np
import math
def calc_angle(x, y):
	norm_x = np.linalg.norm(x)
	norm_y = np.linalg.norm(y)
	cos_theta = np.dot(x, y) / (norm_x * norm_y)
	try:
		theta = math.degrees(math.acos(cos_theta))
		return theta
	except:
		pass

def file_read(filename):
	values = []
	file = open(filename, "r") 
	for line in file:
    		values.append(line)
	values = [line.rstrip('\n') for line in values]
	return values
def Strings(filename):
	Splitted = []
	main = []
	x = file_read(filename)
	for k in x[0::]:
		x = k.split()
		x = list(map(int , x))
		Splitted.append(x)	
	return Splitted	
def generate_array(filename):
	main = []
	x = Strings(filename)
	y = x[0][1]
	for k in range(0, y):
		main.append([])
	return main 
def generate_nulls(filename):
	main = generate_array(filename)
	x = Strings(filename)
	y = x[0][0]
	for k in main:
		for j in range(0,y):
			k.append(0)
	main = np.array(main)
	return main
def inc(filename):
	main = generate_nulls(filename)
	x = Strings(filename)
	y = x[0][1]
	for a in x[1::]:
		try:
			main[int(a[1])-1][int(a[0])-1] = 1
		except:
			pass
	return main
def degrees(filename):
	main=inc(filename)
	angles=[]
	for i in range(0, len(main)):
		for k in range(1, len(main)):
			if i == k:
				pass
			else:angles.append(sorted((i+1, k+1, round(calc_angle(main[i], main[k]), 2))))
	return angles
def eliminating(filename):
	angles=degrees(filename)
	result = [list(x) for x in set(tuple(x) for x in angles)]
	return result 
def sorted_by_angle(filename):
	angles=eliminating(filename)
	angles.sort(key = lambda angles: angles[0]) 
	return angles

def item_matches_angle(filename, filename2, number):
	angles=sorted_by_angle(filename)
	queries = Strings(filename2)
	item_query = []
	ang = []
	for i in queries:
		item_query.append(i) 
	for k in angles:
		if number == k[0] or number == k[1]:
			ang.append(k[2])
	ang = sorted(ang, key=float)
	return ang
def item_match(filename, filename2, number):
 	ang = item_matches_angle(filename,filename2, number)
 	angles = sorted_by_angle(filename)
 	for a in angles:
 		if ang[0] == a[2]:
 			if int(number) == int(a[1]):
 				return int(a[0])
 			elif int(number) == int(a[0]):
 				return int(a[1])
def interface(filename, filename2):
	angles = sorted_by_angle(filename)
	length = len(eliminating(filename))
	current_purchase = Strings(filename2)
	ave = []
	averageangle = 0
	print("Positive entries: " + str(length))
	for angle in angles:
		ave.append(angle[2])
	for k in ave:
		averageangle = averageangle + k
	averageangle = averageangle / len(ave)
	print("Average angle: " + str(round(averageangle, 2)))
	for x in current_purchase:
		recommendation = []
		print("Shopping cart: " + str(x))
		for a in x:
			b = item_match(filename, filename2, a)
			c = item_matches_angle(filename, filename2, a)
			if min(c) == 90:
			 	print("Item: " + str(a) + " No match")
			elif min(c) != 90 and c[1] == 90:
				if b in x:
					if c[1] == 90:
						print("Item: " + str(a) + " No match")
					if str(b+1) in recommendation:
						pass
					else:
						recommendation.append(str(b+1))
				else:
					print("Item: " + str(a) + "; "+ "Match:" + str(b) + "; "  + "Angle:" + str(c[0]))
					if str(b) in recommendation:
						pass
					else:
						recommendation.append(str(b))
			else:
				if b in x:
					print("Item: " + str(a) + "; "+ "Match:" + str(b+1) + "; "  + "Angle:" + str(c[1]))
					if str(b+1) in recommendation:
						pass
					else:
						recommendation.append(str(b+1))
				else:
					print("Item: " + str(a) + "; "+ "Match:" + str(b) + "; "  + "Angle:" + str(c[0]))
					if str(b) in recommendation:
						pass
					else:
						recommendation.append(str(b))
		print("Recommendation: " + str(recommendation))
print(interface("history.txt", "queries.txt")) #The alghorithm takes 2 files. 
#First is the primary file, around which we build the angles, the seconds is the current purchases that we are recomending items to.
#Since Sublime was used, there may be an indentation error.
