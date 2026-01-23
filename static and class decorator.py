class MathOperations:
    @staticmethod
    def add(x, y):      
        return x + y
    @staticmethod
    def multiply(x, y):
     
        return x * y
result_add = MathOperations.add(5, 3)
result_multiply = MathOperations.multiply(4, 6)
print(f"The sum is: {result_add}")
print(f"The product is: {result_multiply}")
calc_instance = MathOperations()
result_instance_add = calc_instance.add(1, 1)
print(f"The sum using an instance is: {result_instance_add}")


