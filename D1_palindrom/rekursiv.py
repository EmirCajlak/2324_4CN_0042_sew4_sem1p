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

    max_value_list = max(m_list)
    max_value_dict = max(m_dict.values())
    max_position_list = m_list.index(max_value_list)
    max_position_dict = max(m_dict, key=m_dict.get)

    print(f"Maximalwert in m_list: {max_value_list} an Position {max_position_list}")
    print(f"Maximalwert in m_dict: {max_value_dict} an Position {max_position_dict}")

    # Dauer der Berechnung
    t0 = time()
    print(t0)