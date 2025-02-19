# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#  Determines the output shape and operation count of a fully-connected layer
# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors

# Output:
#  Prints the output channel count, output height count, output width count, number of additions performed, number of multiplications performed, number of divisions performed 
#
# Written by Kristin Eickelbeck
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_in = float('nan') #input channel count
n_wv = float('nan') #number of weight vectors


# parse script arguments
if len(sys.argv)==3:
   c_in = float(sys.argv[1])
   n_wv = float(sys.argv[2])  
else:
   print(\
    'Usage: '\
    'python3 full_ops.py c_in n_wv'\
   )
   exit()

# write script below this line
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed


