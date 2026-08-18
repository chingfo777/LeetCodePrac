class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Built-in find returns the lowest index or -1 if not found
        return haystack.find(needle)