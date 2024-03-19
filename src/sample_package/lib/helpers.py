# src/code/lib/helber.py
import random

def get_answer() -> bool:
    """Get an answer."""
    return True

def generate_random_number():
    """
    Generates a random 5-digit number.
    """
    return random.randint(10000, 99999)

def generate_uuid(max_groups=5, separator='-') -> str:
    """
    Generates a UUID based on a random 5-digit number.
    
    Args:
        max_groups (int): Maximum number of UUID groups.
        separator (str): Separator between UUID groups.
    
    Returns:
        str: Generated UUID.
    """
    return separator.join(str(generate_random_number()) for _ in range(max_groups))