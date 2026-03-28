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

    def run_app(self):
        """
        Handles the User Interface logic, including keyboard input,
        input validation, and displaying results.
        """
        
        print("GCD Calculator")
        
        #simple tap in
        val1 = input("please enter the first number")
        val2 = input("please enter the second number")
        
        #check and make sure only entering number
        if val1.isdigit() and val2.isdigit():
            num1 = int(val1)
            num2 = int(val2)
            #Ensure numbers are greater than zero as per Euclidean rules
            if num1 > 0 and num2 >0:
                result = self.calculate_gcd(num1, num2)
                print(f"The Greatest Common Divisor is: {result}")
            else:# Error handling for zero or negative values
                print("please enter number greater than zero. ")
        else:# Error handling for non-numeric inputs
            print("Invalid input! Please enter whole numbers only.")
# Main entry point of the application            
if __name__ == "__main__":
    solver = EuclideanAlgorithm()
    solver.run_app()

