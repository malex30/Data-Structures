class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # I'm not sure if a while loop would have been better here 
        # but I choose to go with a for loop since I feel more comfortable
        # at this point. As well I know this problem is better attacked 
        # with a Hash Map (dictionary) while will make this more efficient.

        # Since in Python a string is an object I can iterate through it
        # so I look for the current letter in magazine using an if statement
        for letter in ransomNote:
            if letter in magazine:
                # because print is always a good tool to understand what is going on
                print(letter)
                # at first I forgot the replace function will replace ALL characters
                # in question, I googled how to select an occurrence and found this page
                # https://stackoverflow.com/questions/4628618/replace-first-occurrence-of-string-in-python
                magazine = magazine.replace(letter, "",1)
                print(magazine)
                # break if statement and continue to for loop if char was found
                continue
            else:
                # if not that means the solution can not be solved so return False
                return False
        return True


# time complexity o(n^2) because I interate through each index of two arrays
# space complexity o(1) because no new data structure is proportionally created