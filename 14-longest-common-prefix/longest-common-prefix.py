class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as the base reference
        prefix = strs[0]
        
        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Shorten prefix until s starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix
        