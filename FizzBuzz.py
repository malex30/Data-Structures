class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # variables to add to string
        FizzBuzz = "Fizzbuzz"
        Fizz = "Fizz"
        Buzz = "Buzz"
        # an empty list
        answer = []

        for x in range(1,n+1):
            # run through n times starting with 1 as the index
            print(x)
            #if statement to find remaining of modules
            # to show 0 starting with 0 and 5
            if x % 3 == 0 and x % 5 == 0:
                answer.append("FizzBuzz")
                print(answer)
            elif x % 3 == 0:
                answer.append("Fizz")
                print(answer)
            elif x % 5 == 0:
                answer.append("Buzz")
                print(answer)
            else:
                answer.append(str(x))
        return answer

# time complexity o(n) because interate 1 - n
# space complexity o(1) because no new data structure is proportionally created

