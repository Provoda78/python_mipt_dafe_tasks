def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num <= 1:
        print(1)
    elif num > 1:
        for i in range(1, num-1):
            factorial *= i
    return factorial
