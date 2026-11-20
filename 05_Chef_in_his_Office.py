# Chef in his Office
## LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/OFFICE

## CODE:
t = int(input())

for i in range(t):
    x,y = list(map(int, input().split()))
    print(x*4+y)

## EXPLANATION
"""
input number of test cases.
x is working hours from monday to thursday so total is x*4
and y is working hour on friday.
total hours = x*4 + y
"""
