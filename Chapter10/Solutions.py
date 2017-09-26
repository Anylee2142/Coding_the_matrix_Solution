import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one
from vec import Vec
from mat import Mat
from echelon import *

from vecutil import *
from matutil import *
from orthogonalization import *
from solver import solve

def find_V(U,W):
    # Return V that U's orthogonal complement space to W
    # U = list that vectors
    # W = list that vectors

    W_basis=orthogonalize(W)
    U_basis=orthogonalize(U)

    L = U_basis + W_basis

    ortho_results=orthogonalize(L)

    # After orthogonalize(L), delete U's entries
    # Then V remains.
    for each in range(len(U_basis)):
        ortho_results.remove(ortho_results[0])

    remove_idx=[]
    for idx,val in enumerate(ortho_results):
        # If certain entry's square itself is less than e-20,
        # we assume that entry is 0-vector
        if val*val <= 1e-20:
            remove_idx.append(idx)

    remove_entry=[ortho_results[i] for i in remove_idx]
    for each in remove_entry:
        ortho_results.remove(each)

    return ortho_results

