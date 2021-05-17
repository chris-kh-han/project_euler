# **_Project Euler_** 🐍

## <span style="color:red">Number 5</span> 👉 

 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

[Link](https://projecteuler.net/problem=5)

## _Solution_ 👇 

```python
import math


def lcm(n):
    result=1
    for i in range(1,n+1):
      result=int(math.fabs(result*i)/math.gcd(result,i))
      
    print(result)
 


if __name__ == '__main__':
  lcm(20)

# Return 232792560
```