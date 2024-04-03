# a = 1
# b = 2
# c = a + b
# c = str(c)
# print(type(c))
# bool("hello")
# x = None
# print(x)
# print(type(x))
# names = ['Sonam', 'Pema', 'karma']
# names.append('Phurba')
# print(names)
# names1 = {1, 'sonam'}
# names2 = {'lemo', 3, 'sonam'}
# unionnames = names1.union(names2)
# differnames = names2.difference(names1)
# print(unionnames)
# print(differnames)


# # Outer loop
# for i in range(1, 4):  # Iterating over values 1, 2, 3
#     # Inner loop
#     for j in range(i):  # Iterating over values based on the current value of i
#         print(f"Outer loop iteration {i}, Inner loop iteration {j+1}")


# # Outer for loop
# for i in range(3):  # Iterating over values 0, 1, 2
#     print(i)
  
    
#     # Inner while loop
#     j = 0
#     while j < 2:  # Inner loop continues while j is less than 2
#         print(j+1)
#         j += 1
        
# def func():
#     print(x)
# x=200    
# func()
# # print(x)
# def greet(): # Function definition 
#     print('Hello, Welcome aboard!') # Function body
    
# greet() # function call




# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(2))
# print(my_function(5))

# def add_numbers():
#     sum = 5 + 4
    
# def myfunc():
#   x = 100
#   print(x)

# myfunc()

# x = 100

# def myfunc():
#   print(x)

# myfunc()

# print(x)

# def func():
#     s = "Me too!"
#     print(s)
 
# # Global scope
# s = "I love Python"

# func()
# print(s)



def myfunc1():
  x = "Pema"  # Assigning "Pema" to variable x within myfunc1's scope

  def myfunc2():
    # nonlocal x  # Declaring x as nonlocal to modify the variable in myfunc1's scope
    x = "hello"  # Assigning "hello" to x, which now affects the outer function's x

  
  myfunc2() 
  return x # Calling myfunc2, which modifies the value of x
#  # Returning the modified value of x ("hello")

print(myfunc1())  # Calling myfunc1 and printing the returned value

# This is a recursive function
#to find the factorial of an integer

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))


num = 3
print("The factorial of", num, "is", factorial(num))

# for i in range(1,7,2):
#     for j in range(i):
#         print(i,j+1)


# def update(x: int) -> int:
#     return x + 0.0001

# def main():
#     x = 1
#     while x < 11:
#         x = update(x)
#         print("Wakanda")

# main()

# while True:
#     print("This is an infinite loop")
    
    
# x = 0
# while x < 5:  # Termination condition: loop executes while count is less than 5
#     print(x)
#     x += 1  # Increment count
# for _ in []:
#     print("This is an infinite loop")

# import itertools

# # Infinite loop using for loop
# for _ in itertools.count():
#     print("This is an infinite loop")