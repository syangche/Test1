# def am_odd(n):
#     def calc(x):
#         return x * x
#     total = 0
#     for i in range(1, n + 1):
#         total += calc(i)
#     return total

# print(am_odd(4)) # 1*1 + 2*2 + 3*3 = 14


# def am_odder(n):
#     def calc(x, y):
#         return x + y
#     total = 0
#     for i in range(1, n + 1):
#         total = calc(total, i)
#     return total
# print(am_odder(4)) # 1 + 2 + 3 = 6

# def am_oddest(n):
#     def calc():
#         total = 0
#         for i in range(1, n + 1):
#             total += i * i
#         return total
#     return calc()

# print(am_oddest(4)) # 1*1 + 2*2 + 3*3 = 14

# from typing import List
# def do_something(len: int, a: List[int]) -> None:
#     curr = 0
#     while curr < len:
#         if curr == 0 or a[curr] >= a[curr - 1]:
#             curr += 1
#         else:
#             temp = a[curr]
#             a[curr] = a[curr - 1]
#             a[curr - 1] = temp
#             curr -= 1
            
# print(do_something(3,[3,1,2]))

# x = 100
# y = x

# print(id(x))
# print(id(y))

# x = 2
# x = x + 1
# print(x)

# def myFunc(a):
#   print("Value received in 'a' =", a)
#   a += 2
#   print("Value of 'a' changes to :", a)
  
# num = 13
# print("value of number before function call: ", num)
# myFunc(num)
# print("Value of number after function call= ", num)

# def myFunc(myList):
#   print("List received: ", myList)
#   myList.append(3)  # Add 3 to the end of the list
#   myList.extend([7, 1])  # Extend the list with [7, 1]
#   print("List after adding some elements:", myList)
  
#   myList.remove(7)  # Remove the first occurrence of 7
#   myList[:] = [3, 4, 6]  # Reassign the list (effectively modifying the original list)
#   print("List within called function:", myList)

# List1 = [1]
# print("List before function call :", List1)
# myFunc(List1)
# print("List after function call: ", List1)

# print("hello", end = " ")
# print("world")

# def sod(n):
#     if n < 10:
#         return n
#     else:
#         last_digit = n % 10
#         remaining = n // 10
#         return (last_digit + sod(remaining))
    
# print(sod(23))

