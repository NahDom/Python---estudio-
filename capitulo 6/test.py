"""Test for a not gate"""

def not_gate(input: int) -> int:
    if input == 1:
        return 0
    else:
        return 1

if __name__ == "__main__":
    import doctest

    doctest.testmod()