import re
from typing import Callable


def generator_numbers(text: str):
    # Find all numbers separated by spaces
    pattern = r'(?<!\S)\d+(?:\.\d+)?(?=\s|$)'

    # Search for all matching numbers in the text
    for number in re.findall(pattern, text):
        # Convert the string into a float and yield it
        yield float(number)


def sum_profit(text: str, func: Callable):
    # Calculate the total sum of all generated numbers
    total = sum(func(text))

    # Return the total profit
    return total


# Example usage
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

# Calculate the total income
total_income = sum_profit(text, generator_numbers)

# Print the result
print(f"Загальний дохід: {total_income:.2f}")
