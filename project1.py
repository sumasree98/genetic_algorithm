import random
import math
sensors=[]
length=1000
breadth=1000
number_sensors=200
no_col_points=40
range1=100
index=0
for i in range(0,number_sensors):
	x=random.randint(0,1000)
	y=random.randint(0,1000)
	sensors.append([x,y])
range_=100
col_points=[]
for i in range(0,no_col_points):
	x=random.randint(0,1000)
	y=random.randint(0,1000)
	col_points.append([x,y])
membership=[]
for i in range(0,number_sensors):
	distance=[]
	for j in range(0,no_col_points):
		dist=math.sqrt((sensors[i][0]-col_points[j][0])**2+(sensors[i][1]-col_points[j][1])**2)
		distance.append(dist)
	min_dist=min(distance)
	j=0
	for j in range(0,no_col_points):
		if(distance[j]==min_dist):
			break
	membership.append(j)
c=0
while c==0:
	for i in range(0,no_col_points):
		centroid1=0
		centroid2=0
		number=0
		for j in range(0,number_sensors):
			if(membership[j]==i):
				number+=1
				centroid1+=sensors[j][0]
				centroid2+=sensors[j][1]
		if(number==0):
			continue
		centroid1/=number
		centroid2/=number
		col_points[i][0]=centroid1;
		col_points[i][1]=centroid2;
	check=0;
	for i in range(0,number_sensors):
		distance=[]
		for j in range(0,no_col_points):
			dist=math.sqrt((sensors[i][0]-col_points[j][0])**2+(sensors[i][1]-col_points[j][1])**2)
			distance.append(dist)
		min_dist=min(distance)
		j=0
		for j in range(0,no_col_points):
			if(distance[j]==min_dist):
				break
		if(membership[i]!=j):
			check=1
			membership[i]=j
	if(check==0):
		break

total=0
for i in range(0,number_sensors):
	dist=math.sqrt((sensors[i][0]-col_points[membership[i]][0])**2+(sensors[i][1]-col_points[membership[i]][1])**2)
	if(dist<=range1):
		total+=1
list.sort(sensors)
total_distance=0
for i in range(0,no_col_points-1):
	dist=math.sqrt((col_points[i][0]-col_points[i+1][0])**2+(col_points[i][1]-col_points[i+1][1])**2)
	total_distance+=dist
print "number of sensors covered: ",total
print "total distance: ",total_distance
