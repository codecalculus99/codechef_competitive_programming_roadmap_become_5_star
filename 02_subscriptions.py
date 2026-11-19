## Subscriptions
## LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUBSCRIBE_

## CODE
import math
t = int(input())

for i in range(t):
    n,x = list(map(int, input().split()))
    if n <= 6:
        print(x)
    else:
        print(math.ceil((n/6))*x)


## EXPLANATION
"""
First line takes number of test cases a input.
That many times the loop will run.
Takes two inputs (n,x) from the user.
Check whethe the number of people (n) is greater than 6 or not if not
then it will prin the cost (x) given.
Otherwise it will take divide the total number of people(n) by 6 and then rounded up and multiply with cost (x) to get the final
susbscription price.
"""
        
        
        
