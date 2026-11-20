# Mahasena
## LINK: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AMR15A

## CODE:
n = int(input())
arr = list(map(int, input().split()))

even = odd = 0

for i in arr:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
        
if even > odd:
    print('READY FOR BATTLE')
else:
    print('NOT READY')


## EXPLANATION
"""
take n as number of soldiers as input.
Count number of even values and odd values.
If even > odd then READY else NOT READY
"""
