# Water Filling
## LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WATERFILLING

## CODE
t = int(input())

for i in range(t):
    b1, b2, b3 = list(map(int, input().split()))
    
    if (b1+b2+b3) >= 2:
        print("Not now")
    else:
        print("Water filling time")

