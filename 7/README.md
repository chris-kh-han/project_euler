# **_Project Euler_** 🐍

## <span style="color:red">Number 7</span> 👉 

 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

[Link](https://projecteuler.net/problem=7)

## _Solution_ 👇 

```python
def prime(n):
  primes_arr = [2]
  start = 3
  while len(primes_arr) < n:
    is_prime = True
    for prime in primes_arr:
      if start % prime == 0:
        is_prime = False
        break;
      
    if is_prime:
      primes_arr.append(start)
    start = start + 2

  print(primes_arr[n-1])

 
prime(10001)
      

# Return 104743
```