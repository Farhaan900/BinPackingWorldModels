import numpy as np

# raw_data = np.load("record/47374336.npz")['obs']
# print(raw_data)
# print(np.shape(raw_data))
# print(len(raw_data))
# x = np.array([1,2,3,4,5,6])
# print(x)
# zeroso = np.zeros([5,5,2])
# print(zeroso)
#
# xid = 0
# for y in x:
#     zeroso[xid/5][xid%5] = y
#     xid += 1
#
# print(zeroso)

new_list = []
list = [[1,2], [3,4]]

for x in list:
    new_list.append([[y] for y in x])

print(new_list)