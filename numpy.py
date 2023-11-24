import numpy as np

simple_list = [1,2,3,4]

np_arr = np.array(simple_list)

print(np_arr)

print("------------ Vector ----------")

my_vector = np.array(["this","is","vector"])

print(my_vector)

print("------------ Matrix ----------")

m_matrix = [[1,2,3,4],[2,4,6,8],[1,3,5,7]]

my_matrix = np.array(m_matrix)

print(my_matrix)

print("------------ Numpy Array: Builtin Methods ----------")

a_rrange = np.arange(0,5)

print("arrange methods:",a_rrange)

ss_range = np.arange(1,11,2)

print("Step-Size of array:",ss_range)

a_zeros = np.zeros(5)

print("Array of zeros:",a_zeros)

m_zeros = np.zeros([5, 5])

print("Matrix array of zeros:",m_zeros)

i_arr = np.linspace(0,1,10)

print("Interval for numbers using Numpy:",i_arr)

identical_arr = np.eye(3)

print("Identical Array:",identical_arr)

