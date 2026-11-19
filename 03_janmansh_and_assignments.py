## Janmansh and Assignments
## LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/JASSIGNMENTS

## CODE
t = int(input())

for i in range(t):
    x = int(input())
    if (x+3) <= 10:
        print('Yes')
    else:
        print('No')


## EXPLANATION
"""
First line takes number of test cases.
It will run for that many test cases.
Now there are three assignments and each assignments takes 1 hr each.
If x + 3 is under 10 then Yes else No
"""
