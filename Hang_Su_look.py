import sys
import os
if os.path.isfile(sys.argv[1])==False:
	print("error, no such file")
	exit()
f=open(sys.argv[1])
# f=open("queue4.txt")
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
track.sort()
min=200
for i in track:
	if i==head:
		schedule.append(i)
track=list(filter(lambda a:a!=head,track))
nexthead=head
if track==[]:
	print(",".join(str(i) for i in schedule))
	print(cost)
	exit()
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
if nexthead-head>0:
	preDirection=False
if head-nexthead>0:
	preDirection=True

if preDirection:
	if track[-1]>head:
		cost=head-track[0]+track[-1]-track[0]
		schedule+=list(reversed(track[0:track.index(nexthead)+1]))+track[track.index(nexthead)+1:]
	else:
		cost=head-track[0]
		schedule+=list(reversed(track))
if preDirection==False:
	if track[0]<head:
		cost=track[-1]-head+track[-1]-track[0]
		schedule+=track[track.index(nexthead):]+list(reversed(track[0:track.index(nexthead)]))
	else:
		cost=track[-1]-head
		schedule+=track
print(",".join(str(i) for i in schedule))
print(cost)