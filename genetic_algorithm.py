import random
import math
sensors=[]
length=1000
breadth=1000
index=0
number_sensors=250
no_genes=20
collection_points=40
for i in range(0,number_sensors):
	x=random.randint(0,1000)
	y=random.randint(0,1000)
	sensors.append([x,y])
range_=100
gen=[]
for i in range(0,40):
	gen.append([])
def generate(gen):
	for i in range(0,20):
		for j in range(0,collection_points):
			x=random.randint(0,1000)
			y=random.randint(0,1000)
			gen[i].append([x,y])
def fit1(gen1,sensors):
	fitness1=0
	for i in range(0,number_sensors):
		for j in range(0,collection_points):
			d=math.sqrt((sensors[i][0]-gen1[j][0])**2+(sensors[i][1]-gen1[j][1])**2)
			if(d<=range_):
				fitness1+=1
				break
	return (fitness1)
def sort1(gen):
	for i in range(0,40):
		list.sort(gen[i])
def sort(gen,no_genes,sensors):
	fit2=[]
	for i in range(0,no_genes):
		fitness=fit1(gen[i],sensors)
		fit2.append(fitness)
	for i in range(1,no_genes):
		temp=fit2[i]
		temp1=gen[i]
		j=i-1
		while(temp>fit2[j] and j>=0):	
			fit2[j+1]=fit2[j]
			gen[j+1]=gen[j]
			j-=1
		fit2[j+1]=temp
		gen[j+1]=temp1
def check(gen):
	for i in range(0,40):
		for j in range(i+1,40):
			if(gen[i]==gen[j]):
				pos=random.randint(0,collection_points-1)
				x=random.randint(0,1000)
				y=random.randint(0,1000)
				gen[j][pos][0]=x
				gen[j][pos][1]=y
def crossover(gen,no_genes,sensors):
	low=0
	high=no_genes-1
	index=20
	while(high>low):
		gen[index]=[]
		gen[index+1]=[]
		r=random.randint(0,collection_points-1)
		for i in range(0,r):
			gen[index].append(gen[high][i])
			gen[index+1].append(gen[low][i])
		for i in range(r,collection_points):
			gen[index].append(gen[low][i])
			gen[index+1].append(gen[high][i])
		low+=1
		high-=1
		index+=2
	sort1(gen)
	sort(gen,40,sensors)
	check(gen)
	sort1(gen)
	sort(gen,40,sensors)
def mutate(gen,no_genes):
	for i in range(0,no_genes):
		x=random.randint(0,50)
		if(x==25):
			pos=random.randint(0,collection_points-1)
			x=random.randint(0,1000)
			y=random.randint(0,1000)
			gen[i][pos][0]=x
			gen[i][pos][1]=y
generate(gen)
sort1(gen)
sort(gen,no_genes,sensors)
for i in range(0,120):
	crossover(gen,no_genes,sensors)
for i in range(0,20):
	print gen[i]
	print fit1(gen[i],sensors)
	print " "
mutate(gen,no_genes)
sort1(gen)
sort(gen,no_genes,sensors)
f=fit1(gen[0],sensors)
print 'number of sensors and distance: ', f
