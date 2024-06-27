
def square(x):
  return x * x 

def map_multiple(func, my_list):
   result = []
   for i in my_list:
      result.append(func(i))
   return result 


squares = map_multiple(square, [1,2,3,4,5])
print()