def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False