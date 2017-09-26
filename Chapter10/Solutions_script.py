from Solutions import *
# 10.11.1
# Because of floating point calculation,
# if val*val == 0 or <=1e-20 then val == 0

# If two vectors are inner-bounded when result == 0,
# two vectors are orthogonal

# 1.
W = [list2vec(v) for v in [[1, 2, -3, -1], [1, 2, 0, 1], [3, 1, 0, -1], [-1, -2, 3, 1]]]
U = [list2vec(v) for v in [[0, 0, 3, 2]]]
V = find_V(U, W)

# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 2.
W = [list2vec(v) for v in [[1, 0, 0], [1, 0, 1]]]
U = [list2vec(v) for v in [[3, 0, 1]]]
V = find_V(U, W)

# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 3.
W = [list2vec(v) for v in [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]
U = [list2vec(v) for v in [[-4, 3, 1, -2], [-2, 2, 3, -1]]]
V = find_V(U, W)

# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)


# 10.11.3
W=[list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]
A=[list2vec(v) for v in [[-4,-3,-2,-1],[0,4,0,-1]]]
V=find_V(A,W)

rowdict={idx:A[idx] for idx in range(len(A))}
M=rowdict2mat(rowdict)
coldict={idx:V[idx] for idx in range(len(V))}
null_space=coldict2mat(coldict)

result= M * null_space

# for each in (M*null_space).f.values():
#     print(each*each)

# 10.11.4
# find normal of each line == find orthogonal-complement-space of each line
# 1.
W=[list2vec(v) for v in [[1,0],[0,1]]]
A=[list2vec(v) for v in [[3,2]]]
V_of_A=find_V(A,W)
# for each in V_of_A:
#     print(each)
#     print(each*A[0])

# 2.
B=[list2vec(v) for v in [[3,5]]]
V_of_B=find_V(B,W)
# for each in V_of_B:
#     print(each)
#     print(each*B[0])

# 10.11.5
# 1.
W=[list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
U=[list2vec(v) for v in [[0,1,0],[0,0,1]]]
V=find_V(U,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 2.
U=[list2vec(v) for v in [[2,1,-3],[-2,1,1]]]
V=find_V(U,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 3.
alpha=list2vec([3,1,4])
beta=list2vec([5,2,6])
gamma=list2vec([2,3,5])
U=[alpha-beta, alpha-gamma]
V=find_V(U,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 10.11.6
# 1.
W=[list2vec(v) for v in [[1,0],[0,1]]]
V=[list2vec(v) for v in [[0,7]]]
U=find_V(V,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 2.
V=[list2vec(v) for v in [[1,2]]]
U=find_V(V,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 10.11.7
# 1.
W=[list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
V=[list2vec(v) for v in [[0,1,1]]]
U=find_V(V,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

# 2.
V=[list2vec(v) for v in [[0,1,0]]]
U=find_V(V,W)
# for v in V:
#     for u in U:
#         val=v*u
#         print(val**2)

