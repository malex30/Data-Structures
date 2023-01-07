class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        # I want an initial "rich customer" to compare to
        richest_customer = 0

        #  I want to interate through the list given 
        # starting with the first index "i"  
        for i in accounts:
            # I need a new variable to establish the customer
            # currently working through
            customer_total = 0
            for j in i:
                # I want to add to the customer_total with each account
                customer_total += j
                print(customer_total + j)
            # after totaling the customers accounts we need to 
            # compare to the current richest_customer
            # which initially will be 0 which is why I use 0 to start
            if customer_total >= richest_customer:
                richest_customer = customer_total
        return richest_customer 

# time complexity o(n^2) because I interate through each index of two arrays
# space complexity o(1) because no new data structure is proportionally created