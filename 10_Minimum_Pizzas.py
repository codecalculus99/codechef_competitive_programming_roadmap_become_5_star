# Minimum Pizzas
## https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINPIZZA

## Code
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    total_slices = n * x
    pizzas = (total_slices + 3) // 4

    print(pizzas)


"""
Complexity
- Time complexity: O(1) per test case
- Space complexity: O(1) extra space
"""

## Competitive Programming Tips
"""
For positive integers, ceiling division means dividing two numbers and rounding up to the nearest integer.
[a/b] = (a+b-1)/b which is equivalent to math.ceil(a/b)
"""
