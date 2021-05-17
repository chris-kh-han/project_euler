# **_Project Euler_** 🐍

## <span style="color:red">Number 6</span> 👉 

 
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

[Link](https://projecteuler.net/problem=6)

## _Solution_ 👇 

```python
import math


def diff(n):
  square_of_sum = sum([x for x in range(1, n+1)])**2
  sum_of_square = sum([x**2 for x in range(1, n+1)])

  print(square_of_sum - sum_of_square)

if __name__ == '__main__':
  diff(100)

# Return 25164150
```