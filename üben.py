s = "hallo"
s = s[::2]
print(s)

"""
l1 = ["emir", "cajlakovic", "mike", "rolo"]
>>> uneven = [i for i in range (10,2)]
"""


def is_palindrom(s: str) -> bool:
    """
    Check if a string is a palindrome.

    :param s: Input string
    :return: True if s is a palindrome, False otherwise

    Examples:
    >>> is_palindrom("9009")
    True
    >>> is_palindrom("-1")
    False
    >>> is_palindrom("Teset")
    False
    >>> is_palindrom("TeseT")
    True
    >>> is_palindrom("TesET")
    False
    """

    reversedStr: str = ""
    for c in reversed(s):
        reversedStr += c

    return s == reversedStr


def is_palindrom_sentence(s: str) -> bool:
    """
    Check if a sentence is a palindrome, considering only letters and ignoring spaces and punctuation.

    :param s: Input sentence
    :return: True if s is a sentence palindrome, False otherwise

    Examples:
    >>> is_palindrom_sentence("Oh, Chello! Voll Echo!")
    False
    >>> is_palindrom_sentence("Oh, Cello! Voll Echo!")
    True
    >>> is_palindrom_sentence("oof")
    False
    >>> is_palindrom_sentence("fuf")
    True
    """

    # filter string
    s = "".join(filter(str.isalnum, s)).lower()

    reversedStr: str = ""
    for c in reversed(s):
        reversedStr += c

    return s == reversedStr


def palindrom_product(x: int) -> int:
    """
    Find the largest palindrome number (smaller than x) that is the product of two 3-digit numbers.

    :param x: Maximum limit
    :return: The largest palindrome product

    Examples:
    >>> palindrom_product(1000000)
    906609
    >>> palindrom_product(20000)
    19591
    >>> palindrom_product(-1)
    0
    """

    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrom(str(product)) and product < x and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome


def get_dec_hex_palindrom(x: int) -> int:
    """
    Find the largest number (smaller than x) that is a palindrome in both decimal and hexadecimal representations.

    :param x: Maximum limit
    :return: The largest decimal and hexadecimal palindrome

    Examples:
    >>> get_dec_hex_palindrom(50000)
    41514
    >>> get_dec_hex_palindrom(320)
    11
    >>> get_dec_hex_palindrom(555412)
    512215
    >>> get_dec_hex_palindrom(-1)
    0
    """

    largest_palindrome = 0
    for i in range(1, x):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            largest_palindrome = i
    return largest_palindrome


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem
    :return: Zahl im Zielsystem als String

    Examples:
    >>> to_base(1234, 16)
    '4D2'
    >>> to_base(42, 2)
    '101010'
    >>> to_base(123456, 8)
    '361100'
    """

    # safety check
    if base < 2 or base > 36:
        raise ValueError("Base should be between 2 and 36.")

    if number == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number > 0:
        number, remainder = divmod(number, base)
        result = digits[remainder] + result
    return result


def main() -> None:
    """
    Main Method
    """
    pass


if __name__ == "__main__":
    main()

"""
:Author: Viktor Trojan
"""

from time import time


def M(n: int) -> int:
    """
    Compute M(n) recursively.

    M(n) is defined as follows:
    - M(n) = M(M(n + 11)) if n ≤ 100
    - M(n) = n - 10 if n > 100

    :param n: Input number
    :return: Result of M(n)

    Examples:
    >>> M(95)
    91
    >>> M(100)
    91
    >>> M(101)
    91
    >>> M(110)
    100
    >>> M(290)
    280
    >>> M(68290)
    68280
    >>> M(-792)
    91
    >>> M(3)
    91

    """
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10


def main() -> None:
    """
    Main Method
    """

    # Calc time taken
    t0 = time()

    # Gen a list with 200 elements containing the results of M(n)
    m_list = [M(n) for n in range(200)]

    # Gen a dict with 200 elements where keys are n and values are M(n)
    m_dict = {n: M(n) for n in range(200)}

    elapsed_time = time() - t0
    print(f"Time taken: {elapsed_time} seconds")

    # Time taken: 0.003002166748046875 seconds


if __name__ == "__main__":
    main()