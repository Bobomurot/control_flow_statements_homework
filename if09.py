def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    n = a // 10
    n1 = a % 10
    a1 = n1 * 10 + n
    if a >= a1:
        return True
    else:
        return False
