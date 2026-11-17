n = "aura"
n1 = 1
result = 1
result1 = 0

while isinstance(n, str) or isinstance(n, bool) or isinstance(n, float):
    n = int(input("Please input the number of fibonacci's sequence you want to obtain \n(Ex: n4 = 2)"))


if (n <= 2):
    if (n == 2):
        print("Your result is", result + 1)
    else:
        print("Your result is", result)
else:
    while n1 != n:
        result, result1 = result + result1, result
        print(result, result1)

        n1 = n1 + 1

print("Your result it", result)
