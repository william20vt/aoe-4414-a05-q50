# ray_sphere_intersection.py
#
# Usage: python3 ray_sphere_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z c_s_x c_s_y c_s_z r_s
#  
# Parameters:
#  d_l_x, d_l_y, d_l_z: direction vector of origin-referenced ray unit vector
#  c_l_x, c_l_y, c_l_z: coordinates of the rau origin offset
#  c_s_x, c_s_y, c_s_z: coordinates of the sphere origin offset
#  r_s: sphere radius
# Output:
#  Print the x, y, and z coordinates of the intersection point if it exits
#
# Written by William Sosnowski
# Other contributors: Github Copilot and Nathan Griffin
#
# See the LICENSE file for the license.

# import Python modules
import math # math module
import sys 

# "constants"
# R_E_KM = 6378.1363  # Earth's equatorial radius in km
# E_E = 0.081819221456  # Earth's eccentricity
# w = 7.2921159e-5 # Earth's rotation rate in rad/s
# sol_day = 86400 # number of seconds in a day

# helper functions

## vector magnitude
def mag(v):
    # sum_of_squares=0.0
    # for i in range(0,len(v)):
    #     sum_of_squares += v[i]**2
    # return math.sqrt(sum_of_squares)
    return math.sqrt(sum([i**2 for i in v]))

##scalar multiplication
def smul(s,v):
    # sprod = []
    # for i in range(0, len(v)):
    #     sprod.append(s*v[i])
    return [s*i for i in v]

##vector addition
def vadd(v1, v2):
    # sum = []
    # for i in range(0, len(v1)):
    #     sum.append(v1[i]+v2[i])
    if len(v1) != len(v2):
        return None
    else:
        # v3 = []
        # for i in range(len(v1)):
        #     v3.append(v1[i] + v2[i])
        # return v3
        return [v1[i]+v2[i] for i in range(len(v1))]

##vector subtraction
def vsub(v1, v2):
    # diff = []
    # for i in range(0, len(v1)):
    #     diff.append(v1[i]-v2[i])
    if len(v1) != len(v2):
        return None
    else:
        # v3 = []
        # for i in range(0,len(v1)):
        #     v3.append(v1[i] - v2[i])
        # return v3
        return [v1[i]-v2[i] for i in range(len(v1))]

def dot(v1, v2):
    if len(v1) != len(v2):
        return float('nan')
    else:
        # dp=0.0
        # for i in range(0,len(v1)):
        #     dp += v1[i]*v2[i]
        # return dp
        return sum([v1[i]*v2[i] for i in range(len(v1))])

def cross(v1, v2):
    return [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]

# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')
c_s_x = float('nan')
c_s_y = float('nan')
c_s_z = float('nan')
r_s = 6378137

if len(sys.argv) != 10:
        print("Usage: python3 ray_sphere_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z c_s_x c_s_y c_s_z r_s")
        sys.exit(1)
else:
        d_l_x = float(sys.argv[1])
        d_l_y = float(sys.argv[2])
        d_l_z = float(sys.argv[3])
        c_l_x = float(sys.argv[4])
        c_l_y = float(sys.argv[5])
        c_l_z = float(sys.argv[6])
        c_s_x = float(sys.argv[7])
        c_s_y = float(sys.argv[8])
        c_s_z = float(sys.argv[9])
   #     r_s = float(sys.argv[10])
    
d_l = [d_l_x, d_l_y, d_l_z] #must be a unit vector
c_l = [c_l_x, c_l_y, c_l_z] #must be a unit vector
c_s = [c_s_x, c_s_y, c_s_z] #must be a unit vector
    
cl_m_cs = vsub(c_l, c_s)
a = dot(d_l, d_l)
b = 2*dot(d_l, cl_m_cs)
c = dot(cl_m_cs, cl_m_cs) - r_s**2
discr = b**2 - 4*a*c
    
if discr >= 0:
        d = (-b - math.sqrt(discr))/(2*a)
if d < 0.0:
            d = (-b + math.sqrt(discr))/(2*a)
if d >= 0.0:
            l_d = (smul(d, d_l)+c_l)
            print(f"{l_d[0]:.6f}")
            print(f"{l_d[1]:.6f}")
            print(f"{l_d[2]:.6f}")
            



