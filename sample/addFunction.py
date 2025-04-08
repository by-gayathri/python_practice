def add_ten(n):
    n = n + 10
    return n


num1 = input('Enter the number: ')
result = add_ten(float(num1))
print("The added result: {0} ".format(result))
