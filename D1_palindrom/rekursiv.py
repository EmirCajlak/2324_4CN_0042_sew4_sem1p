"""
Author: Emir Cajlakovic 4CN
04.12.2023
UE04
"""
def M(n):
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10