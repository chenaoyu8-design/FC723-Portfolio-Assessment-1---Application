class EuclideanAlgorithm:
    """ this class encapsulates the Euclidean Algoeithm to calculate the 
    Greatst Common Divisor of two integers."""
    def calculate_gcd(self,a,b):
        """Implements the core logic of the Euclidean Algorithm."""
        while b!=0:
            remainder = a % b
            a = b
            b = remainder
        return a

#function test
if __name__ == "__main__":
    solver = EuclideanAlgorithm()
    #input number to test 
    print(f"test result (48,18):{solver.calculate_gcd(48,18)}")