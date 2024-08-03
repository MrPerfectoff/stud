immutable_var = ([1, 2, 3], 'string', 1, 2, True, 3.5 )
print(immutable_var)
immutable_var[0][0] = 3
print(immutable_var)
mutable_list = ['one', 'two', 'three']
mutable_list[2] = 'peach'
print(mutable_list)