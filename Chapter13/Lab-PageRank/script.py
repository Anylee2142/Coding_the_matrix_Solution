from Solutions import *

#test case
D = set(range(1,7))
f = [(1,1),(1,4),(2,3),(2,4),(2,5),(2,6),(3,2),(4,5),(5,6),(6,5)]
small_links = Mat((D, D), {x:1 for x in f})
A2= Mat(small_links.D, {(r, c):1/6 for r in small_links.D[0] for c in small_links.D[1]})

tmp=sum(1 for each in range(3))

tmp=Vec({1,2,3},{1:1,2:0,3:1})

A1=make_Markov(small_links)

v=power_method(0.85*A1+0.15*A2,10000)

# 13.12.3
# approximate eigen-vector of v1 for stationary-distribution
# whose eigen-value is 1
print(v)

# 13.12.4
# type this in console, not execution
links=read_data()
titles=find_word('jordan')

# 13.12.6
A=make_Markov(links)
p=power_method(A,100)
best=wikigoogle('jordan',5,p)