import sys
sys.path.append("D:\Python\Matrix")

from vecutil import *
from matutil import *
from eigenfaces import *
from orthogonalization import *
from solver import *
import svd
import itertools

# 12.6.1
faces=load_images('faces')
D0=set(range(166))
D1=set(range(189))
D=set(itertools.product(D0,D1))

a={k:Vec(D,{d:pixel[d[1]][d[0]] for d in D}) for k,pixel in faces.items()}

# 12.6.2
centroid=sum(vec for vec in a.values())/len(a)
centering={k : vec - centroid for k,vec in a.items()}

# 12.6.3

# A is faces
A=rowdict2mat(centering)
U,sigma,V=svd.factor(A)

coldictV={k:basis for k,basis in mat2coldict(V).items()}
k=10
best_k_basis=[coldictV[i] for i in range(k)]
eigenface=coldict2mat({k:col_vec for k,col_vec in enumerate(best_k_basis)})

# k X (166*189)

# 12.6.4
def projected_representation(x,M):
    # transpose(Q)*b
    # Refer to the page 421
    return transpose(M)*x

# 12.6.5
def projection_length_squared(x,M):
    # 439~440 page
    x_v=projected_representation(x,M)
    return x_v*x_v

# 12.6.6
def distance_squared(x,M):
    # b_v = b - b||v
    # 12.6.6 = x*x - 12.6.5
    return x*x - projection_length_squared(x,M)

# 12.6.7
# distances_from_eigenface=[distance_squared(centering_image,eigenface)
#                           for centering_image in centering.values() ]

def a(x):
    return 2/3*x**3 - 3*x**2 + 4*x

