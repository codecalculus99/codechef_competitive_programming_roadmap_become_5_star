## GREATER AVERAGE
## PROBLEM LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AVGPROBLEM

## CODE
t = int(input())

for i in range(t):
    a,b,c = list(map(int, input().split()))
    if (a+b)/2 > c:
        print('YES')
    else:
        print('NO')


## EXPLANATION
"""
First line take number of test cases as input.
Then that many times the loop will run.
Take three values in the same line (a,b,c).
Check whether the average of a and b is strictly greater than c or not.
"""
