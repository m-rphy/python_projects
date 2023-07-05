#  compute the fibonacci number

#  The input will be the index n of the fibonacci series
#  and the output should be F(n)


#  This is a dynamic programming solution that utilizes the
#  the bottom up approach for a linear problem
#  The space compexity is O(1) and time complexity is O(n)
def F(n):
    #  This is the "cache" that will hold
    #  previously computed values
    results = [0, 1]
    #  These two conditionals handle the
    #  edge cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Inititalizing a counter variable to
    i = 1
    while i < n:
        #  iteratively find the sum of our
        #  results arr
        sum = results[0] + results[1]
        #  and update the results array
        #  to hold the prvious el at arr[1] and
        # the newly computed sum
        results = [results[1], sum]
        #  then incrementing i
        i += 1
    # return the last sum => F(n)
    return sum


print(F(5))  # 0, 1, 1, 2 , 3
