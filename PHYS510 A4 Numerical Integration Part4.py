"""
Created on Thu Jun 13 20:47:04 2013
PHYS 510, Assignment 4 Part 4
"""

# Numerical Integration
"""
This assignment is to develop algorithms for numerical integration using the following methods:
    4. Gauss-Legendre Quadrature 
Use the algorithms to evaluate the following integrals:
    1. Int[sin(x)*exp(x)], x = -pi to pi
    2. Int[x*exp(x**2)], x = -1 to 1
    3. Int[1/(1+x**2)], x= -4 to 4
Make a result table and compare your numerical result to the analytical solution by finding the relative 
percent error for each method.
"""

from sympy import *

# Part 4
# Gauss-Legendre method
#*******************************************************************
def Gauss(g, a, b, n):
    f = lambda x: eval(g)    # define function to evaluate
    
    # Gauss-Legendre lists in function below only goes to n = 12
    if n > 12: print 'NUMBER OF POINTS TO EVALUATE MUST BE LESS THAN 12'
    
    # get abscissas (xi), and weights (wi) from function below
    # GaussLegendre function below has values of xi and wi up to n = 12
    abscissa, weight = GaussLegendre(n)   
    intSum = 0
    
    # Gauss-Legendre method is valid only over interval [-1,1]
    # check if integral is over [-1,1], if so do as normal
    # if not, need to map interval [a,b] to [-1,1]
    if a == -1 and b == 1:
        for i in range(n):
            intSum = intSum + weight[i]*f(abscissa[i])  # evaluate integral
        
        print 'Gauss Integral = ', intSum
            
    # if interval not [-1,1], map input [a,b] to [-1,1]
    else:
        sx = Symbol('sx')             # define symbolic variable x
        x = 0.5*(b-a)*sx + 0.5*(b+a)  # change of variables to map [a,b] to [-1,1]
        
        sf = eval(g)                  # create new symbolic function over [-1,1]
        f = lambdify(sx, sf)          # turn symbolic function into real function
        
        for i in range(n):
            intSum = intSum + weight[i]*f(abscissa[i])  # evaluate integral
        
        print 'Gauss Integral = ', 0.5*(b-a)*intSum
                    

#Gauss('sin(x)*exp(x)',-pi, pi, 10)
#Gauss('x*exp(x**2)',-1.0, 1.0, 10)
#Gauss('1/(1+x**2)', -4.0, 4.0, 10)
#-------------------------------------------------------------------
# g = 'function of x' entered in quotes (Ex. 'sin(x)')
# a = integration region x start point (entered as decimal)
# b = integration region x end point (entered as decimal)
# n = number of points to generate and evaluate (up to n = 12)
#------------------------------------------------------------------- 
#*******************************************************************


# the function below stores the abscissas (xi) and weights (wi) 
# for the Gauss-Legendre integration method for integration over [-1,1]
#*******************************************************************
def GaussLegendre(n):
    if n == 2:
        xi = [-0.5773502691896257, 0.5773502691896257]
        wi = [1.0000000000000000, 1.0000000000000000]
        
    if n == 3:
        xi = [0.0000000000000000, -0.7745966692414834, 0.7745966692414834]
        wi = [0.8888888888888888, 0.5555555555555556, 0.5555555555555556]
        
    if n == 4:
        xi = [-0.3399810435848563, 0.3399810435848563, -0.8611363115940526,
              0.8611363115940526]        
        wi = [0.6521451548625461, 0.6521451548625461, 0.3478548451374538, 
              0.3478548451374538]
              
    if n == 5: 
        xi = [0.0000000000000000, -0.5384693101056831, 0.5384693101056831,
              -0.9061798459386640, 0.9061798459386640]
        wi = [0.5688888888888889, 0.4786286704993665, 0.4786286704993665,
              0.2369268850561891, 0.2369268850561891]
              
    if n == 6:
        xi = [0.6612093864662645, -0.6612093864662645, -0.2386191860831969,
              0.2386191860831969, -0.9324695142031521, 0.9324695142031521]
        wi = [0.3607615730481386, 0.3607615730481386, 0.4679139345726910,
              0.4679139345726910, 0.1713244923791704, 0.1713244923791704]
              
    if n == 7:
        xi = [0.0000000000000000, 0.4058451513773972, -0.4058451513773972,
              -0.7415311855993945, 0.7415311855993945, -0.9491079123427585,
              0.9491079123427585]
        wi = [0.4179591836734694, 0.3818300505051189, 0.3818300505051189,
              0.2797053914892766, 0.2797053914892766, 0.1294849661688697,
              0.1294849661688697]
              
    if n == 8:
        xi = [-0.1834346424956498, 0.1834346424956498, -0.5255324099163290,
              0.5255324099163290, -0.7966664774136267, 0.7966664774136267,
              -0.9602898564975363, 0.9602898564975363]
        wi = [0.3626837833783620, 0.3626837833783620, 0.3137066458778873,
              0.3137066458778873, 0.2223810344533745, 0.2223810344533745,
              0.1012285362903763, 0.1012285362903763]
              
    if n == 9:
        xi = [0.0000000000000000, -0.8360311073266358, 0.8360311073266358,
              -0.9681602395076261, 0.9681602395076261, -0.3242534234038089,
              0.3242534234038089, -0.6133714327005904, 0.6133714327005904]
        wi = [0.3302393550012598, 0.1806481606948574, 0.1806481606948574,
              0.0812743883615744, 0.0812743883615744, 0.3123470770400029,
              0.3123470770400029, 0.2606106964029354, 0.2606106964029354]
              
    if n == 10:
        xi = [-0.1488743389816312, 0.1488743389816312, -0.4333953941292472,
              0.4333953941292472, -0.6794095682990244, 0.6794095682990244,
              -0.8650633666889845, 0.8650633666889845, -0.9739065285171717,
              0.9739065285171717]
        wi = [0.2955242247147529, 0.2955242247147529, 0.2692667193099963,
              0.2692667193099963, 0.2190863625159820, 0.2190863625159820,
              0.1494513491505806, 0.1494513491505806, 0.0666713443086881,
              0.0666713443086881]
              
    if n == 11:
        xi = [0.0000000000000000, -0.2695431559523450, 0.2695431559523450,
              -0.5190961292068118, 0.5190961292068118, -0.7301520055740494,
              0.7301520055740494, -0.8870625997680953, 0.8870625997680953,
              -0.9782286581460570, 0.9782286581460570]
        wi = [0.2729250867779006, 0.2628045445102467, 0.2628045445102467,
              0.2331937645919905, 0.2331937645919905, 0.1862902109277343,
              0.1862902109277343, 0.1255803694649046, 0.1255803694649046,
              0.0556685671161737, 0.0556685671161737]
              
    if n == 12:
        xi = [-0.1252334085114689, 0.1252334085114689, -0.3678314989981802,
              0.3678314989981802, -0.5873179542866175, 0.5873179542866175,
              -0.7699026741943047, 0.7699026741943047, -0.9041172563704749,
              0.9041172563704749, -0.9815606342467192, 0.9815606342467192]
        wi = [0.2491470458134028, 0.2491470458134028, 0.2334925365383548,
              0.2334925365383548, 0.2031674267230659, 0.2031674267230659,
              0.1600783285433462, 0.1600783285433462, 0.1069393259953184,
              0.1069393259953184, 0.0471753363865118, 0.0471753363865118]
        
    return xi, wi
#*******************************************************************