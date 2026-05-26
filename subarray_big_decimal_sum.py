# =============================================
# HackerRank Assessment - Subarray Big Decimal Sum
# =============================================
# Problem:
# You are given an array of strings `nums` where each string represents a non-negative
# decimal number (can be very large).
#
# Given two indices `left` and `right`, return the sum of all numbers in the subarray
# nums[left..right] as a string.
#
# You cannot convert strings to int/float or use BigInteger libraries.
#
# Requirements (from email):
# - Efficient algorithm (time and space complexity)
# - Handle padding left/right, align decimals, same length with 0s, remove trailing 0s
# - Clean, modular code is encouraged
# - 15 test cases expected

from typing import List

def add_big_decimals(a: str, b: str) -> str:
    """Helper: Add two big decimal strings. Implement this first."""
    # TODO: Implement big decimal addition here
    # Use the hints: pad right, pad left, handle decimal point carefully

    #handle empty input
    if not a or not b:
        return "0"

    def split_number(num):
        if "." not in num:
            return num, ""
        whole, decimal = num.split(".")
        return whole, decimal

    #split nums into whole and decimal
    a_whole, a_dec = split_number(a)
    b_whole, b_dec = split_number(b)

    #pad decimal right with ljust(length, "0")
    dec_length = max(len(a_dec), len(b_dec))
    a_dec = a_dec.ljust(dec_length, "0")
    b_dec = b_dec.ljust(dec_length, "0")

    #pad whole left with zfill(length)
    whole_length = max(len(a_whole), len(b_whole))
    a_whole = a_whole.zfill(whole_length)
    b_whole = b_whole.zfill(whole_length)

    print(f"{a_whole} . {a_dec}, {b_whole} . {b_dec}")

    #combine both into a string without decimal to perform addition
    a_string = a_whole + a_dec
    b_string = b_whole + b_dec
    string_len = len(a_string)

    #add right to left with carry
    result = []
    carry = 0

    for i in range(string_len - 1, -1, -1):
        digit_sum = int(a_string[i]) + int(b_string[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10

    result.reverse()
    digits = ''.join(result)

    #add decimal into the string
    dec_pos = len(digits) - dec_length
    #for cases like 0.009
    if dec_pos <= 0:
        # Result is less than 1
        digits = '0' * (-dec_pos) + digits
        dec_pos = 0
    whole_part = digits[:dec_pos]
    dec_part = digits[dec_pos:]

    #rstrip 0 from dec, then construct result string
    if dec_part:
        dec_part = dec_part.rstrip('0')
        result_str = f"{whole_part}.{dec_part}"
    else:
        result_str = whole_part if whole_part else "0"

    #lstrip 0 from result string, then check if 0 is needed in the front
    result_str = result_str.lstrip('0')
    if result_str[0] == '.':
        result_str = '0' + result_str
    #not really needed but just in case bad result
    if not result_str or result_str == ".":
        result_str = "0"

    return result_str


def subarray_big_decimal_sum(nums: List[str], left: int, right: int) -> str:
    """
    Return the sum of nums[left..right] as a string.
    """
    # TODO: Implement here.
    # You can use the helper above.
    # Consider: Is there a more efficient way than adding one by one if ranges are large?
    pass


# debug
print(add_big_decimals("12345.31", "67.9876"))

# =============================================
# Test Cases
# =============================================
# if __name__ == "__main__":
#     test_cases = [
#         # Basic
#         (["123", "456", "78.9"], 0, 2, "657.9"),
#         (["1.1", "2.2", "3.3"], 0, 2, "6.6"),
#
#         # With large numbers and different decimal places
#         (["999999999.99", "0.01", "1.2345"], 0, 2, "1000000001.2345"),
#
#         # Edge cases
#         (["0.000", "0", "0.00"], 0, 2, "0"),
#         (["123.45000", "67.89100"], 0, 1, "191.341"),
#         ([".5", "0.5", "0.000"], 0, 2, "1"),
#         (["5.", "10", "0.0"], 0, 2, "15"),
#
#         # Single element subarray
#         (["123.456"], 0, 0, "123.456"),
#
#         # Large subarray
#         (["1.1"] * 10, 0, 9, "11"),
#     ]
#
#     for i, (nums, left, right, expected) in enumerate(test_cases, 1):
#         result = subarray_big_decimal_sum(nums, left, right)
#         status = "PASS" if result == expected else "FAIL"
#         print(f"Test {i}: sum({nums[left:right+1]}) = {result}  [{status}]")