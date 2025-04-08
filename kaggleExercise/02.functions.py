# help(round)
# help(round(-2.01))
#
#
# def least_difference(a, b, c):
#     """Return the smallest difference between any two numbers
#     among a, b and c.
#     """
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     min(diff1, diff2, diff3)
#
#
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7),
# )
#
#
# # 2nd
# def greet(who="Colin"):
#     print("Hello,", who)
#
#
# greet()
# greet(who="Kaggle")
# # (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
# greet("world")
#
#
# # 3rd
# def mult_by_five(x):
#     return 5 * x
#
#
# def call(fn, arg):
#     """Call fn on arg"""
#     return fn(arg)
#
#
# def squared_call(fn, arg):
#     """Call fn on the result of calling fn on arg"""
#     return fn(fn(arg))
#
#
# print(
#     call(mult_by_five, 1),
#     squared_call(mult_by_five, 1),
#     sep='\n',  # '\n' is the newline character - it starts a new line
# )
#
# # 4
# print(1, 2, 3, sep=' < ')
#
#
# # 5
# def mod_5(x):
#     """Return the remainder of x after dividing by 5"""
#     return x % 5
#
#
# print(
#     'Which number is biggest?',
#     max(100, 51, 14),
#     'Which number is the biggest modulo 5?',
#     max(100, 51, 14, key=mod_5),
#     sep='\n',
# )

# num = round(19.987, -2)
# print(num)

# total_candies = 1
# test = total_candies % 3
# print(test)
#
# # More short hands
# print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
# a = 5
# b = 6
# a, b = b, a

# print(int(False))
# d = [1, 2, 3][1:]
# print(d)
# print(len(d))


# def elementwise_greater_than(L, thresh):
#     """Return a list with the same length as L, where the value at index i is
#     True if L[i] is greater than thresh, and False otherwise.
#
#     # >>> elementwise_greater_than([1, 2, 3, 4], 2)
#     [False, False, True, True]
#     """
#     final = [ele > thresh for ele in L]
#     print(final)
#
#
# elementwise_greater_than([2, 3, 4, 5], 2)


# def menu_is_boring(meals):
#     """Given a list of meals served over some period of time, return True if the
#     same meal has ever been served two days in a row, and False otherwise.
#     """
#     for i in range(len(meals)-1):
#         if meals[i] == meals[i + 1]:
#             print("boring")
#             return True
#     return False
#
#
# menu_is_boring(["briyani", "rasam", "rasam"])


string = "12345"

print(string.isdigit())  #Checks for whole string
