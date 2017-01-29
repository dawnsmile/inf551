import sys
import os
if os.path.isfile(sys.argv[1])==False:
	print("error, no such file")
	exit()
f=open(sys.argv[1])
head=int(f.readline())
tmp=f.readline()
while (tmp=="\n"):
	tmp=f.readline()
track=[int(i) for i in tmp.split(",")]
f.close()

cost=0
schedule=[]
preDirection=True
if head>99:
	preDirection=False
while len(track)>0:
	min=200
	nexthead=head
	for i in track:
		if abs(i-head)==min:
			if i-head<0:
				if preDirection:
					nexthead=i
			if i-head>0 and preDirection==False:
				nexthead=i	
		if abs(i-head)<min:
			min=abs(i-head)
			nexthead=i

	schedule.append(nexthead)
	if nexthead-head<0:
		preDirection=True
	if nexthead-head>0:
		preDirection=False
	head=nexthead
	cost+=min
	track.remove(nexthead)

print(",".join(str(i) for i in schedule))
print(cost)