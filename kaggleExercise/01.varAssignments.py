spam_amount = 0
print(spam_amount)
print(type(spam_amount))
print(type(19.09))

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)


# Operator	Name	Description
# a + b	Addition	Sum of a and b
# a - b	Subtraction	Difference of a and b
# a * b	Multiplication	Product of a and b
# a / b	True division	Quotient of a and b
# a // b	Floor division	Quotient of a and b, removing fractional parts
# a % b	Modulus	Integer remainder after division of a by b
# a ** b	Exponentiation	a raised to the power of b
# -a	Negation	The negative of a

# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
print(min(1, 2, 3))
print(max(1, 2, 3))
print(abs(32))
print(abs(-32))
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
