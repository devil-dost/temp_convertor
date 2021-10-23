def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

val = input("Enter your value: to convert in F to C ")
print(convert(val))
