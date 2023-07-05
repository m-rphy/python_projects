#  memoization and caching or true dynamic solution -> NOPE
#  bottom up dynamic programming solution -> Oh Ya!!


def climbStairs(n):
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


print(climbStairs(5))
