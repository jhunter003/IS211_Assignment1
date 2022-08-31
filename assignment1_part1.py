def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count


class ListDivideException(Exception):
    pass


def test_list_divide():
    """
    Test list_divide
    """
    if not list_divide([1, 2, 3, 4, 5]) == 2:
        raise ListDivideException("1st error")
    if not list_divide([2, 4, 6, 8, 10]) == 5:
        raise ListDivideException("2nd error")
    if not list_divide([30, 54, 63, 98, 100], divide=10) == 2:
        raise ListDivideException("3rd error")
    if not list_divide([]) == 0:
        raise ListDivideException("4th error")
    if not list_divide([1, 2, 3, 4, 5], 1) == 5:
        raise ListDivideException("5th error")


test_list_divide()
