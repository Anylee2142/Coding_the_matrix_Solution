def increments(L): return [each+1 for each in L]

def cubes(L): return [each**3 for each in L]

def tuple_sum(A,B): return [(a[0]+b[0],a[1]+b[1]) for a,b in zip(A,B)]

A=[(1,2),(10,20)]
B=[(3,4),(30,40)]

# print(tuple_sum(A,B))

def inv_dict(d): return{v:k for (k,v) in d.items()}

# print(inv_dict({'qwer':1234,'rew':'435'}))

def row(p,n): return [p+each for each in range(n)]

# print(row(20,15))

def row_second(i,j): return [row(1,20)[i:i+j]]

# print(tmp_second(3,10))

def row_third(i,j,p,n): return [p+each for each in range(n)][i:i+j]

# print(row_third(3,10,1,20))

