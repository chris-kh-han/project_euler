# **_Project Euler_** 🐍

## <span style="color:red">Number 4</span> 👉 

 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

[Link](https://projecteuler.net/problem=4)

## _Solution_ 👇 

```python
_range = range(100,1000)
result = 0

for x in _range:
  for y in _range:
    palin = x * y
    if str(palin) == str(palin)[::-1]:
      if palin > result:
        result = palin

print(result)

# Return 906609
```