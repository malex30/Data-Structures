class Solution:
    def numberOfSteps(self, num: int) -> int:
        original = num
        # initialize variable to count the number of steps
        counter = 0
        # loop through until original is 0
        while original != 0:
            print(f'counter: {counter} and original: {original}')
            # Testing if original is even
            # If so divide in half and run through while loop
            if original % 2 == 0:
                original //= 2
                print(counter)
            # if not even. It must be odd so subtract by 1
            else:
                original -= 1
                print(counter)
            counter += 1
        print(counter)
        #return counter "steps"
        return counter