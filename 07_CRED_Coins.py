# CRED Coins
### LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CREDCOINS

## CODE:
t = int(input())

for i in range(t):
    x,y = list(map(int, input().split()))
    print(x*y//100)


