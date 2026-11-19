# Exams
## LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/EXAMCHEF

## CODE:
t = int(input())

for i in range(t):
    x,y,z = list(map(int, input().split()))
    if (z/(x*y))*100 > 50:
        print('YES')
    else:
        print('NO')


## EXPLANATION
"""
First takes number of test cases.
That many times loop will run.
Takes three inputs namely x,y,and z.
If number of students passed is strictly greater than 50% then 
Yes else No.
"""
