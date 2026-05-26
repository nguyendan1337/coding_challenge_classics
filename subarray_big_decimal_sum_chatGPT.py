"""
HackerRank Practice Problem: Subarray Big Decimal Sum

Problem:
You are given an array of decimal numbers represented as strings.

Implement:

    def subarray_big_decimal_sum(nums: List[str], left: int, right: int) -> str

Return the sum of nums[left..right] inclusive as a string.

Rules / Constraints:
- Numbers are given as strings and may contain:
    - leading zeros
    - decimal points
    - varying decimal precision
- Do NOT use float conversion because of precision issues.
- Simply converting to numeric types and summing may not be acceptable.
- Normalize numbers by:
    - padding missing decimal places with zeros
    - treating all numbers as fixed-point decimals
- Remove trailing zeros in final decimal result.
- If decimal portion becomes empty, return integer string only.

Efficiency hint:
If range queries are large or repeated, think about prefix sums.

Examples:
Input:
    nums = ["1.2", "03.40", "5"]
    left = 0
    right = 2

Normalized:
    1.2   -> 1.20
    03.40 -> 3.40
    5     -> 5.00

Output:
    "9.6"
"""
from typing import List

def max_sum_sliding_window(nums, k):
    # Step 3: sliding window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

def subarray_big_decimal_sum(nums: List[str], left: int, right: int) -> str:
    """
    Return the sum of nums[left..right] as a string.

    TODO:
    1. Find max decimal precision across all nums
    2. Normalize each string
    3. Convert to fixed-point integers
    4. Build prefix sums
    5. Compute range sum
    6. Convert result back to decimal string
    """

    """
    Return sum of nums[left:right+1] as string.
    Uses prefix sums over normalized fixed-point integers.
    """

    # Find maximum decimal precision
    max_decimals = 0
    for s in nums:
        if "." in s:
            max_decimals = max(max_decimals, len(s.split(".")[1]))

    # Normalize strings -> scaled integers
    values = []
    for s in nums:
        if "." in s:
            int_part, dec_part = s.split(".")
        else:
            int_part, dec_part = s, ""

        dec_part = dec_part.ljust(max_decimals, "0")
        normalized = int_part + dec_part
        values.append(int(normalized))

    # Build prefix sums
    prefix = [0]
    for v in values:
        prefix.append(prefix[-1] + v)

    # Range sum query
    total = prefix[right + 1] - prefix[left]

    # Convert back to string
    total_str = str(total).zfill(max_decimals + 1)

    if max_decimals > 0:
        integer = total_str[:-max_decimals]
        decimal = total_str[-max_decimals:]

        decimal = decimal.rstrip("0")

        if decimal:
            return integer + "." + decimal
        return integer

    return total_str


# =========================
# Test Cases
# =========================
def run_tests():
    tests = [
        {
            "nums": ["1.2", "03.40", "5"],
            "left": 0,
            "right": 2,
            "expected": "9.6",
        },
        {
            "nums": ["0.1", "0.02", "0.003"],
            "left": 0,
            "right": 2,
            "expected": "0.123",
        },
        {
            "nums": ["5", "10", "15"],
            "left": 1,
            "right": 2,
            "expected": "25",
        },
        {
            "nums": ["001.200", "2.300", "3.500"],
            "left": 0,
            "right": 1,
            "expected": "3.5",
        },
        {
            "nums": ["999.99", "0.01"],
            "left": 0,
            "right": 1,
            "expected": "1000",
        },
    ]

    for i, test in enumerate(tests, 1):
        result = subarray_big_decimal_sum(
            test["nums"], test["left"], test["right"]
        )

        passed = result == test["expected"]

        print(f"Test {i}: {'PASS' if passed else 'FAIL'}")
        print(f"Expected: {test['expected']}")
        print(f"Got     : {result}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()