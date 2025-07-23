class EvalFactorial:
    def __init__(self, id, input_data, expected_output):
        self.id = id
        self.input_data = input_data
        self.expected_output = expected_output

    def run(self,fun):
        # if actual_output == self.expected_output:
        #     print("pass")
        # else:
        #     print('Fail')
        try:
            actual = fun(self.input_data)
            status = "Pass" if actual == self.expected_output else "Fail"
        except Exception as e:
            actual = str(e)
            status = "Error"

        print()
        print("Input: ",self.input_data)
        print("Actual Output: ", actual)
        print("Expected Output: ", self.expected_output)
        print("Status: ", status,'\n--------------')



def factorial_pass(num):
    if num < 0: return None
    if num == 0:
        return 1    
    return num * factorial_pass(num-1)

def factorial_fail(num):
    if num > 0: return None
    if num == 0:
        return 1    
    return num * factorial_pass(num-2)

test_cases = [
    EvalFactorial(1,5,120),
    EvalFactorial(2,0,1),
    EvalFactorial(3,-1,None)
]

for tc in test_cases:
    tc.run(factorial_pass)

print("========================")

for tc in test_cases:
    tc.run(factorial_fail)

# print(factorial(5))
# print(factorial(0))
# print(factorial(-1))