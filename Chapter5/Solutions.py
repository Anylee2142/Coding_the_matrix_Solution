import sys
sys.path.append("D:\Python\Matrix")
from vec import Vec
from mat import Mat
from solver import solve
from matutil import *

M=Mat(({'a','b'},{'@','#','?'}),
      {('a','@'):1,('a','#'):2,('a','?'):3,('b','@'):10,('b','#'):20,('b','?'):30})

matrix=Mat(({'a','b','c'},{'a','b','c'}),{('a','a'):1,('b','b'):1,('c','c'):1})

# # 5.1.1
# lists=[[0 for j in range(4)] for i in range(3)]
#
# for row in lists:
#     for each in row:
#         print(each,end='')
#     print()
#
# # 5.1.2
# lists=[[0,-1,-2,-3],[1,0,-1,-2],[2,1,0,-1]]
# col_lists=[[lists[j][i] for j in range(3)] for i in range(4)]
#
# print(col_lists)
#
# for row in col_lists:
#     for each in row:
#         print(each,end='')
#     print()
#
# # 5.1.4
# col=Vec({'a','b'},{'a':3,'b':30})

# # 5.1.5
# coldict={'@':Vec({'a','b'},{'a':1,'b':10}),
#          '#':Vec({'a','b'},{'a':2,'b':20}),
#          '?':Vec({'a','b'},{'a':3,'b':30})}

# # 5.1.7
# matrix=Mat(({'a','b','c'},{'a','b','c'}),{('a','a'):1,('b','b'):1,('c','c'):1})
# print(M.f['a','@'])

# # 5.1.8
# def identity(D): return Mat((D,D),{(D,D):1 for each in D})

# # 5.1.9
# def mat2rowdict(M):
#     return {row : Vec(M.D[1],{col : M.f[row,col] for col in M.D[1]}) for row in M.D[0]}

# # 5.1.10
# def mat2coldict(M):
#     return {col : Vec(M.D[0],{row : M.f[row,col] for row in M.D[0]}) for col in M.D[1]}

# # 5.3.1
# def mat2vec(M): return Vec({key for key in M.f.keys()},M.f)

# # 5.4.2
def transpose(M): return Mat((M.D[1],M.D[0]),{(col,row):M.f[row,col] for row,col in M.f.keys()})

# print(M.D)
# print(M.f)
# print(transpose(M).D)
# print(transpose(M).f)

D={'metal','concrete','plastic','water','electricity'}
v_gnome=Vec(D,{'concrete':1.3,'plastic':.2,'water':.8,'electricity':.4})
v_hoop=Vec(D,{'plastic':1.5,'water':.4,'electricity':.3})
v_slinky=Vec(D,{'metal':.25,'water':.2,'electricity':.7})
v_putty=Vec(D,{'plastic':.3,'water':.7,'electricity':.5})
v_shooter=Vec(D,{'metal':.15,'plastic':.5,'water':.4,'electricity':.8})

rowdict={'gnome':v_gnome,'hoop':v_hoop,'slinky':v_slinky,'putty':v_putty,'shooter':v_shooter}
M=rowdict2mat(rowdict)

# for (k,v) in M.f.items():
#     print(k,v)


b=Vec(D,{'water':373.1,'concrete':312.0,'plastic':215.4,'metal':51.0,'electricity':356.0})
solution=solve(transpose(M),b)
print(M.D)
print(b.D)

print(solution)

print(solution*M)
print(b)

# 5.10.21
def diag(D,entries): return Mat((D,D),{(d,d):entries[d] for d in D})
N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
# print(N1*u1)
#
# if N1[5,'a']==None:
#       print('1234')
#
# print(mat2rowdict(Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})).items())