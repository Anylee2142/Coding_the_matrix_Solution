import sys
sys.path.append("D:\Python\Matrix")
from matutil import *
from vecutil import *
from mat import Mat
from vec import Vec


# 233 page upper Matrix
# M=listlist2mat([[-1,1,2],[1,2,3],[2,2,1]])
# v=list2vec([1,2,0])
# print(M*v)

# 233 page lower Matrix
# M=listlist2mat([[-5,10],[-4,8],[-3,6],[-2,4]])
# v=list2vec([4,3,2,1])
# print(v*M)

# 5.17.12 , 5.17.13, 5.17.14, 5.17.15
# Solutions are in mat.matrix_vector_mul, mat.vector_matrix_mul

# 5.17.16, 5.17.17
# Solutions are in mat.matrix_matrix_mul

# 5.17.9
# ex) dlist = [ {'a':'apple', 'b':'bear'},{ 'a':1, 'b':2 } ] , k = 'a' , returning ['apple', 1]
def dictlist_helper(dlist,k): return [each[k] for each in dlist]
#
# print(dictlist_helper([{'a':'apple','b':'bear'},{'a':1,'b':2}],'a'))