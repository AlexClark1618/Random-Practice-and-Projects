class semi_empirical_mass_formula:
    """
    This is a class includes various operations involving the semi empirical mass formula.

    Attributes:
        A (int or empty string): Mass Number 
        Z (int or empty string): Atomic Number
    """
    def __init__(self, A, Z):
        self.A = A #Mass Number
        self.Z = Z #Atomic Number

    def nuclear_binding_energy(self, verbose=True):
        """
        Calculates the nuclear binding energy given the values for A and Z
        """

        a1 = 15.8
        a2 = 18.3
        a3 = 0.714
        a4 = 23.2
        
        if self.A%2!=0:
            a5 = 0

        elif self.A%2==0 and self.Z%2==0:
            a5 = 12

        else:
            a5 = -12

        NBE = (a1 * self.A) - (a2 * self.A**(2/3)) - ((a3 * self.Z**2) / self.A**(1/3)) - ((a4 * (self.A - 2 * self.Z)**2) / self.A) + (a5 / self.A**(1/2))


        if verbose:
            print(f"The nuclear binding energy of the element with atomic number {self.Z} and mass number {self.A} is {"%.4f" % NBE} MeV.")

        return NBE
    
    def binding_energy_per_nucleon(self, verbose=True):
        """
        Calculates the nuclear binding energy per nucleon
        """

        BEPN = self.nuclear_binding_energy(verbose=False) / self.A

        if verbose:
            print(f"The binding energy per nucleon of the element with atomic number {self.Z} and mass number {self.A} is {"%.4f" % BEPN} MeV.")

        return BEPN

    def most_stable_nuclei(self):
        """
        Calculates the most stable istope if given Z value. If both Z and A are left empty it calculates the most stable isotope of all elements.
        """
        
        if self.A==' ' and self.Z!=' ':

            A_BEPN_dict = {self.A : self.binding_energy_per_nucleon(verbose=False) for self.A in range(self.Z, (3 * self.Z) + 1)}

            max_BEPN = max(A_BEPN_dict.values())

            for key, value in A_BEPN_dict.items():
                if value == max_BEPN:
                    print (f'The most stable isotope of the element with atomic number {self.Z} has a mass number of {key} with a binding energy per nucleon of {"%.4f" % max_BEPN} MeV.')
        
        elif self.A==' ' and self.Z==' ':
            
            Z_list = [self.Z for self .Z in range(1, 120)]

            Z_A_BEPN_list=[]

            for self.Z in Z_list:

                A_BEPN_dict = {self.A : self.binding_energy_per_nucleon(verbose=False) for self.A in range(self.Z, (3 * self.Z) + 1)}

                max_BEPN = max(A_BEPN_dict.values())

                for key, value in A_BEPN_dict.items():
                    if value == max_BEPN:
                        Z_A_BEPN_list.append((self.Z, key, max_BEPN))

            max_Z_A_BEPN_list = max(Z_A_BEPN_list, key = lambda x: x[2])
            
            print(f'The most stable isotope of all elements has an atomic number of {max_Z_A_BEPN_list[0]} and mass number of {max_Z_A_BEPN_list[1]} with a binding energy per nucleon of {"%.4f" % max_Z_A_BEPN_list[2]} MeV.')
   
        else:
            raise ValueError("Incorrect input")

    

if __name__ == "__main__":        
    B1 = semi_empirical_mass_formula(A=58 , Z=28)
    B2 = semi_empirical_mass_formula(A=' ' , Z=28)
    B3 = semi_empirical_mass_formula(A=' ' , Z=' ')
    B1.nuclear_binding_energy()
    B1.binding_energy_per_nucleon()
    B2.most_stable_nuclei()
    B3.most_stable_nuclei()
