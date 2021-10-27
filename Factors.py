num = int(input("Enter a number of whose Factor you want: "))
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

print_factors(num)