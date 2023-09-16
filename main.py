import numpy as np
from scipy import optimize

arr_raw = np.array([[36837, 52354, 20764], [8969, 12238, 5642], [10178, 14297, 6240], [2824, 2086, 1464]])
arr_res = np.array([[57468, 57008, 56711], [14132, 13672, 16039], [16424, 16368, 17671], [1119, 1120, 1267]])
arr_org = np.array([[54394, 54394, 54394], [13762, 13762, 13762], [17694, 17694, 17694], [1310, 1310, 1310]])
arr_org2 = np.array([54394, 17694, 13762, 1310])
# arr_ratio = []
# arr_center = []

def func(p, x, y):
  a,b,c = p
  return a*(x**2) + b*x + c - y

def caculator_center_point(x, y):
    # Input: vị trí xyz của khối x và y
    # Output: center position of two points and ratio 
    # Initial guess for coefficients
    p0 = np.random.random(3) 

    # Solve using least squares
    res = optimize.leastsq(func, p0, args=(x,y))
    coef = res[0]

    # Print quadratic equation
    # print("Quadratic equation: y = {}x^2 + {}x + {}".format(coef[0], coef[1], coef[2]))


    # Evaluate fit
    y_fit = func(coef, x, 0)
    # print("R-squared: {}".format(1-np.sum((y-y_fit)**2)/np.sum((y-y.mean())**2)))
    return coef

def calibration_chanel(chanel, coef):
    h,w = chanel.shape
    out = np.zeros_like(chanel) 
    # Apply quadratic transformation to each pixel

    for y in range(h):
        for x in range(w):
            # Get pixel coordinates 
            # x_norm = x/w 
            # y_norm = y/h
            
            # Apply quadratic equation
            y = coef[0]*(chanel[y,x]**2) + coef[1]*chanel[y,x] + coef[2] 
            
            # Map to output image
            out[y,x] = y
    return out

def calibration_image(image):

# def avr_center_point(arr_raw, arr_org):
#     arr_center = np.array([0,0,0,0,0,0])
#     arr_ratio = np.array([0,0,0,0,0,0])
#     n = 0
#     for i in range(3):
#         for j in range(3-i):
#             arr_ratio[n], arr_center[n] = caculator_center_point(arr_raw[i,0], arr_raw[3-i,0], arr_org[i,0], arr_org[3-i,0])
#             n = n+1
#     return np.average(arr_ratio), np.average(arr_center)

# print(avr_center_point(arr_raw, arr_org))


# def caculator_norm_point(x, center, ratio):
#     return center - (center - x) * ratio

# print(caculator_norm_point(36837, 6182.0, 2.0))

# def caculator_parameter_to_calibration():

#     r01, c01 = caculator_center_point(0, 1)
#     r02, c02 = caculator_center_point(0, 2)
#     r03, c03 = caculator_center_point(0, 3)

#     r10, c10 = caculator_center_point(1, 0)

#     r12, c12 = caculator_center_point(1, 2)
#     r13, c13 = caculator_center_point(1, 3)

#     r20, c20 = caculator_center_point(2, 0)
#     r21, c21 = caculator_center_point(2, 1)

#     r23, c23 = caculator_center_point(2, 3)

#     ratio = (r01+r02+r03+r10+r12+r13+r20+r21+r23)/9
#     center = (c01+c02+c03+c10+c12+c13+c20+c21+c23)/9
#     return ratio,center

# def calibration(ratio, center, arr_raw):
#     for i in range(4):
#         for j in range(3):
#             arr_res = arr_raw[i,j] + (center[j] - arr_raw[i,j]) * ratio
#     return arr_res


# # print(caculator_center_point(0, 1))

# Generate 4 random points 
# np.random.seed(0)
x = np.array([36837, 8969, 10178, 2824])
y = np.array([54394, 13762, 17694, 1310])

# Define the function to optimize
def func(p, x, y):
  a,b,c = p
  return a*(x**2) + b*x + c - y

# Initial guess for coefficients
p0 = np.random.random(3) 

# Solve using least squares
res = optimize.leastsq(func, p0, args=(x,y))
coef = res[0]

# Print quadratic equation
print("Quadratic equation: y = {}x^2 + {}x + {}".format(coef[0], coef[1], coef[2]))


# Evaluate fit
y_fit = func(coef, x, 0)
print("R-squared: {}".format(1-np.sum((y-y_fit)**2)/np.sum((y-y.mean())**2)))


print(x*x*coef[0] +x*coef[1]+coef[2])