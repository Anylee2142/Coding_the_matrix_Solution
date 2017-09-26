from Lab import *
from matutil import *

# A is matrix that 5211 X 206
# 0~5210

nation=readFile2lists('UN_voting_data.txt')
print('Reading File completed')

coldict_nation=votingList2coldict(nation)
print('Converting list to Col dict completed')


A=coldict2mat(coldict_nation)
print('A completed')

A_T=A.transpose()
print('Transpose of A completed')

print('Calculating similarity started')
M=A_T*A
# upper operation includes same country X same country,
# So we should customize in case of that situation.
print('Calculation completed')
print()
# ----------------------------------------------------------
# M sorted by Ascending order
# sorted_M = 206 X 206
sorted_M=sorted( [(value,key) for key,value in M.f.items() if key[0] != key[1]])
# ----------------------------------------------------------

# 1. Bitter rivals
print("Bitter rivals are ",end='')
print(sorted_M[0])
print()

# 2. Most 10 unsimilar nations
print("most 10 unsimilar nations are below")
print("#---------------------------------")
for idx in range(10):
    print(sorted_M[idx])
print("#---------------------------------")

# 3. Closest nations
print("Closest nations are ",end='')
print(sorted_M[len(sorted_M)-1])