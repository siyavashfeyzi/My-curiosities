"""CountDigit.py"""

""" 
We want to know how many numbers 0 to 9 
there are between two integers and of course together 
with those two numbers.

"""

# The beginning of the numerical range
x = input("Enter the number at the beginning of the interval: ")
x = int(x)

# The number at the end of the numeric range
y = input("Enter the number at the end of the interval: ")
y = int(y)

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Count digits
for i in range(x, y+1):
    if i < 10:
        count[i] += 1
    else:
        while i > 0:
            temp = i % 10
            count[temp] += 1
            i = int(i/10)

# print resuls
for i in range(0, 10):
    print("{} : {}".format(i, count[i]))
