def get_gcd(num1: int, num2: int) -> int:
    def get_gcd(num1: int, num2: int) -> int:
    gcd, n  = 1, 0
    if num2 > num1:
        n = num1
        num1 = num2
        num2 = n
    while gcd > 0:
        gcd = num1 % num2
        num1 = num2
        num2 = gcd
    return num1
