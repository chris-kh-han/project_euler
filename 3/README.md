# **_Project Euler_** 🐍

## <span style="color:red">Number 3</span> 👉 

 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

[Link](https://projecteuler.net/problem=3)

## _Solution_ 👇 

```python
divisor = 2
num = 600851475143

while (num > 1):
  if (num % divisor == 0):
    num /= divisor
  else: 
    divisor += 1

print(divisor)

# Return 6857
```