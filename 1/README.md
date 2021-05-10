# **_Project Euler_** 🐍

## <span style="color:red">Number 1</span> 👉 

* If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

* Find the sum of all the multiples of 3 or 5 below 1000.

    [Link](https://projecteuler.net/problem=1)

## _Solution_ 👇 

```python
def sum_multiple_of_3or5(num) :
  print(sum(([x for x in range(1,num) if x % 3 == 0 or x % 5 == 0])))

sum_multiple_of_3or5(1000)

# Return 233168
```






   

