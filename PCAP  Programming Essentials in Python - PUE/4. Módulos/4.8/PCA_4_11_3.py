line = input("Enter line full of numbers - separate them with spaces: ")
strings = line.split()
sum = 0
try:
    for substr in strings:
        sum += float(substr)
    print("Sum =", sum)
except:
    print("It's not a number:", substr)
