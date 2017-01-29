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

if track[0]>head:
	schedule+=track
	cost=track[-1]-head
if track[-1]<head:
	schedule+=track
	cost=199-head+track[-1]+199
if track[0]<head and track[-1]>head:
	for i in track:
		if i>head:
			break
	schedule+=track[track.index(i):]+track[0:track.index(i)]
	cost=199-head+track[track.index(i)-1]+199
print(",".join(str(i) for i in schedule))
print(cost)