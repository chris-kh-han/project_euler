# **_Project Euler_** 🐍

## <span style="color:red">Number 10</span> 👉 


```
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
```


[Link](https://projecteuler.net/problem=10)

## _Solution_ 👇 


```python

def sum_of_primitives():
  n = 2000000
  prime = [True for i in range(n+1)]
  p = 2
  sum = 0

  while (p * p <= n):

    if (prime[p] == True):
        
        for i in range(p * p, n+1, p):
            prime[i] = False
    
    p += 1

  for p in range(2, n+1):
      if prime[p]:
        sum = sum + p
              
  print(sum)
      

# Return 142913828922
```