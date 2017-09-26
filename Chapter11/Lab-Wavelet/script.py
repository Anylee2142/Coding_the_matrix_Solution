from Solutions import *

# 11.9.1
print(forward_no_normalization([1,2,3,4]))
# print(forward_no_normalization([4,5,3,7,4,5,2,3,9,7,3,5,0,0,0,0]))

# 11.9.2
print(normalize_coefficients(4,forward_no_normalization([1,2,3,4])))

# 11.9.3
print(forward([1,2,3,4]))
# print(forward([4,5,3,7,4,5,2,3,9,7,3,5,0,0,0,0]))

# 11.9.4
print(suppress(forward([1,2,3,4]),1))

# 11.9.5
print(sparsity(forward([1,2,3,4])))
print(sparsity(suppress(forward([1,2,3,4]),1)))

# 11.9.6
D=forward([1,2,3,4])
print(D)
print(unnormalize_coefficients(4,D))
print(forward_no_normalization([1,2,3,4]))

# 11.9.7
D=forward_no_normalization([1,2,3,4])
v=backward_no_normalization(D)
print(v)

# 11.9.8
print(forward([1,2,3,4]))
D=forward([1,2,3,4])
print(backward(D))