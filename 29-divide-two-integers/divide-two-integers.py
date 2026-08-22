class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle overflow edge case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Bitwise subtraction
        while a >= b:
            temp_divisor = b
            shift = 0
            # Double temp_divisor until it is greater than the remaining dividend
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                shift += 1

            # Subtract the largest found chunk and accumulate quotient
            a -= temp_divisor
            quotient += (1 << shift)

        # Apply sign and clamp to 32-bit integer limits
        if negative:
            quotient = -quotient

        return max(MIN_INT, min(MAX_INT, quotient))