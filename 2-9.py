'''Madelung Constant'''

"""
Description: The Madelung Constant appears in calcutions of the total 
            electric potential in a crystalline solid

Notes:
    - i, j, and k are indices used to depict the loaction of a specific atom
    - When the sum of i, j, k is + is will represent a positive charge (sodium for this problem)
    - When the sum of i, j, k is - is will represent a negative charge (chlorine for this problem)

"""

import numpy as np
import timeit

#Constants

ep = 8.85e-12 #Electric permitivity of free space
e = 1.6e-19 #Charge of electron/ proton
a = 0.281e-9 #Ion spacing within lattice (value for NaCl given)

def Madelung_Constant_Formula(i, j, k):
    return 1 / np.sqrt((i**2) + (j**2) + (k**2))

def Direct_Madelung_Constant(L: "Size of crystalline solid cube"):
    
    M = 0
    "Full Lattice"
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                if i==0 and j==0 and k==0:
                    pass

                else:
                    if (i + j + k)%2==0:

                        M += Madelung_Constant_Formula(i, j, k)

                    elif (i + j + k)%2!=0:

                        M += -1 * Madelung_Constant_Formula(i, j, k)

    return M

def Simplified_Madelung_Constant(L):
    """
    Description: Modified version of Direct_Madelung_Contants using the symmetry of crystalline lattice

    Args: 
        L (int): Length of crystalline lattice cube

    Returns:
        Float: Madelung Constant
    """

    M1 = 0
    "Upper Half of Lattice"
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(1, L+1):
                if (i + j + k)%2==0:
                    
                    M1 += Madelung_Constant_Formula(i, j, k)
                    
                elif (i + j + k)%2!=0:
                    
                    M1 += -1 * Madelung_Constant_Formula(i, j, k)
    
    M2 = 0
    "Single Lattice Plane centered at point of interest"
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            k=0
            if i==0 and j==0:
                pass   

            else:
                if (i + j + k)%2==0:
                    
                    M2 += Madelung_Constant_Formula(i, j, k)
                    
                elif (i + j + k)%2!=0:
                    
                    M2 += -1 * Madelung_Constant_Formula(i, j, k)  

    return 2 * M1 + M2    

def Potential(M):

    return (e / (4 * np.pi * ep * a)) * M 

if __name__ == "__main__":
    L=100

    "Here to demonstrate the the improved efficiency of Simplified_Madelung_Constant"
    #print(Direct_Madelung_Constant(L))
    #execution_time = timeit.timeit("Direct_Madelung_Constant(L)", number=1, globals=globals())
    #print(f"Execution time: {execution_time} seconds")

    M = Simplified_Madelung_Constant(L)
    print(M)

    #execution_time = timeit.timeit("Simplified_Madelung_Constant(L)", number=1, globals=globals())
    #print(f"Execution time: {execution_time} seconds")

    print(f'{Potential(M)}eV')

    #execution_time = timeit.timeit("Potential(M)", number=1, globals=globals())
    #print(f"Execution time: {execution_time} seconds")
