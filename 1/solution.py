def sum_multiple_of_3or5(num) :
  print(sum(([x for x in range(1,num) if x % 3 == 0 or x % 5 == 0])))

sum_multiple_of_3or5(1000)