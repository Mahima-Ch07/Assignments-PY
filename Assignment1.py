# 1. Check if a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Find the greater of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater:", a)
elif b > a:
    print("Greater:", b)
else:
    print("Both are equal")


# 4. Find the greatest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)


# 5. Check if a person is eligible to vote (age >= 18).
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 6. Check whether a year is a leap year.
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 7. Check if a character is a vowel or consonant.
ch = input("Enter a character: ")
if len(ch) == 1 and ch.lower() in "aeiou":
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Invalid character")


# 8. Check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible")


# 9. Check if a number is a multiple of both 3 and 7.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple")


# 10. Assign grades based on marks.
marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
    
# 11. Check if a character is uppercase or lowercase.
ch = input("Enter a character: ")
if len(ch) == 1 and ch.isupper():
    print("Uppercase")
elif len(ch) == 1 and ch.islower():
    print("Lowercase")
else:
    print("Invalid character")


# 12. Find whether the entered alphabet is a vowel using if-elif.
ch = input("Enter an alphabet: ").lower()
if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Invalid input")


# 13. Check if three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a > 0 and b > 0 and c > 0 and a+b > c and b+c > a and a+c > b:
    print("Valid triangle")
else:
    print("Invalid triangle")


# 14. Determine the type of triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a <= 0 or b <= 0 or c <= 0 or a+b <= c or b+c <= a or a+c <= b:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# 15. Find the largest among four numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
if a >= b and a >= c and a >= d:
    print("Largest:", a)
elif b >= a and b >= c and b >= d:
    print("Largest:", b)
elif c >= a and c >= b and c >= d:
    print("Largest:", c)
else:
    print("Largest:", d)


# 16. Check whether a number is a three-digit number.
num = int(input("Enter a number: "))
if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 17. Calculate electricity bill using slab rates.
units = int(input("Enter electricity units: "))
if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Bill =", bill)
elif units <= 200:
    bill = 100 * 5 + (units-100) * 7
    print("Bill =", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units-200) * 10
    print("Bill =", bill)


# 18. Calculate income tax based on income slabs.
income = float(input("Enter annual income: "))
if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

if income >= 0:
    print("Income tax =", tax)


# 19. Check if a student passes (minimum 35 marks in each subject).
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Pass")
else:
    print("Fail")


# 20. Find whether a number is within a given range.
num = int(input("Enter a number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
if low <= num <= high:
    print("Within range")
else:
    print("Outside range")


# 21. Build a simple calculator using if-elif-else (+, -, *, /).
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Addition =", a+b)
elif op == '-':
    print("Subtraction =", a-b)
elif op == '*':
    print("Multiplication =", a*b)
elif op == '/':
    if b != 0:
        print("Division =", a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 22. Check if a year is a century leap year.
year = int(input("Enter year: "))
if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century but not leap year")
else:
    print("Not a century year")


# 23. Determine the season based on the month number.
month = int(input("Enter month number: "))
if month in [3, 4, 5]:
    print("Summer")
elif month in [6, 7, 8, 9]:
    print("Monsoon")
elif month in [10, 11]:
    print("Post-monsoon")
elif month in [12, 1, 2]:
    print("Winter")
else:
    print("Invalid month")


# 24. Find the number of days in a month.
month = int(input("Enter month number: "))
year = int(input("Enter year: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month")


# 25. Check whether a password meets minimum conditions.
password = input("Enter password: ")
if len(password) >= 8 and any(ch.isdigit() for ch in password) and any(ch.isalpha() for ch in password):
    print("Valid password")
else:
    print("Invalid password")


# 26. Determine ticket price based on age category.
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age <= 5:
    print("Free ticket")
elif age <= 18:
    print("Ticket price = Rs. 50")
elif age <= 60:
    print("Ticket price = Rs. 100")
else:
    print("Ticket price = Rs. 70")


# 27. Calculate discount based on purchase amount.
amount = float(input("Enter purchase amount: "))
if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

if amount >= 0:
    print("Discount =", discount)
    print("Final amount =", amount-discount)


# 28. Check eligibility for a driving license (age and eyesight condition).
age = int(input("Enter age: "))
eyesight = input("Is eyesight normal? (yes/no): ").lower()
if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")


# 29. Create a login system with username and password validation.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")


# 30. Create a menu-driven program using if-elif-else.
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition =", a+b)
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction =", a-b)
elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication =", a*b)
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Division =", a/b)
    else:
        print("Cannot divide by zero")
elif choice == 5:
    print("Exiting program")
else:
    print("Invalid choice")        