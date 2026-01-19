import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:
    """
    Generates a set of unique sorted random numbers for a lottery.
    Args:
        min_val (int): Minimum possible number (>= 1).
        max_val (int): Maximum possible number (<= 1000).
        quantity (int): Number of digits to choose.
    Returns:
        list: Sorted list of unique numbers or an empty list if parameters are invalid.
    """

    if not (1 <= min_val <= max_val <= 1000) or not (0 < quantity <= (max_val - min_val + 1)):
        return []

    try:
        numbers = random.sample(range(min_val, max_val + 1), quantity)
        return sorted(numbers)
    except (ValueError, TypeError):
        return []


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)