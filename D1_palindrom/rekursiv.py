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

if __name__ == "__main__":
    from time import time

    # m_list mit 200 Elementen
    m_list = [M(n) for n in range(200)]

    # Dictionary m_dict mit 200 Elementen
    m_dict = {n: M(n) for n in range(200)}


    