class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # A second segment of ones exists if and only if '01' appears in s
        return "01" not in s