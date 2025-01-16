def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    p_count = 0
    n_count = 0
    if a > 0:
        p_count += 1
    elif a < 0:
        n_count += 1
    if b > 0:
        p_count += 1
    elif b < 0:
        n_count += 1
    if c > 0:
        p_count += 1
    elif c < 0:
        n_count += 1
    if p_count > n_count:
        return "there are a lot of positive numbers"
    else:
        return "there are a lot of negative numbers"
