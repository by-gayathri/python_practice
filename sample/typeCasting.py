name = "John Doe"
age = 25
gpa = 3.8
is_student = False

print(type(gpa))
print(gpa)
gpa = int(gpa)
print(f"After typeCasting float to int - gpa is: {type(gpa)}")
print(gpa)
age = str(age)
print(f"After typeCasting int to string - age is : {type(age)}")

print(f"bool value for string: {bool(name)}")
newName = ""
print(f"bool value for empty string: {bool(newName)}")
