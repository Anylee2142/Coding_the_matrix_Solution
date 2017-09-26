import matplotlib.pyplot as plt
from plotting import plot
from Solutions import list_dot
import math

# 3.14.8
def convex_repre(pt1,pt2): return [[i/100*pt1[0]+(1-i/100)*pt2[0],i/100*pt1[1]+(1-i/100)*pt2[1]] for i in range(101)]

# plot(convex_repre([-1.5,2],[3,0]),4)
# plot(convex_repre([2,1],[-2,2]),4)

# 3.14.9
u=[[1,0],[0,1],[-1,3],[-1/math.sqrt(2),1/math.sqrt(2)]]
v=[[5,4321],[12345,6],[5,7],[1/math.sqrt(2),-1/math.sqrt(2)]]

for x,y in zip(u,v):
    print(list_dot(x,y))