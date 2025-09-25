def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    if num % 2 == 0:
        for _ in range(num // 2):
            multiplications_amount += 1
        return multiplications_amount - 1
    else:
        for _ in range((num-1) // 2):
            multiplications_amount += 1
        return multiplications_amount
