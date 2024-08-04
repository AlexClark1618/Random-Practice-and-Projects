'''Quantum Potential Step'''

import numpy as np

# User Controlled Variables

m = 9.11e-31 #Particle mass

E = 10.5 #Particle Energy

V = 10 #Step Potential

h = 6.58e-16 #h-bar in eV

#Initial wavevector
k1 = np.sqrt(2*m*E) / h

#Transmission wavevector
k2 = np.sqrt(2*m*(E - V)) / h

def trans_prob():

    return (4 * k1 *k2)/(k1 + k2)**2


def refl_prob():

    return ((k1 - k2)/(k1 + k2))**2

if E <= V:
    print("R=1") #Relfection coefficient will always be one
    print("T=0")

if E > V:
    print(f'R={refl_prob()}')
    print(f'T={trans_prob()}')