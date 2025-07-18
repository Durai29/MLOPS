class EvalPalindrome:
    def __init__(self,id,input,expected_output):
        self.id = id
        self.input = input
        self.expected_output = expected_output

    def run(self,func):
        try:
            actual = func(self.input)
            status = "Pass" if actual == self.expected_output else "Fail"
        except Exception as e:
            actual = str(e)
            status = "Error"
        print()
        print("Input: ", self.input)
        print("Expected output: ",self.expected_output)
        print("Your Output: ", actual)
        print("Status: ", status,'\n')

test_cases = [
        EvalPalindrome(1,'madam',True),      # string len -> odd
        EvalPalindrome(2,'anna', True),      # string len -> even
        EvalPalindrome(3,'i$i$i',True),      # speacial character
        EvalPalindrome(4,'Durai',False)      # Not a palindrome
]
        
def palindrome_correct(string):
    return string[::-1] == string

def palindrome_wrong(string):
    return False


for tc in test_cases:
    tc.run(palindrome_correct)

print("-----------------------------------------")

for tc in test_cases:
    tc.run(palindrome_wrong)