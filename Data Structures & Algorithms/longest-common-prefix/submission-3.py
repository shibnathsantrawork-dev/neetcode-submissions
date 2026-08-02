class Solution:
    def longestCommonPrefix(self, strs):
        # Assume the first string is the common prefix
        prefix = strs[0]

        # Compare the prefix with every other string
        for word in strs[1:]:

            i = 0

            # Compare characters one by one
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1

            # Keep only the matching part
            prefix = prefix[:i]

            # If nothing is common, return immediately
            if prefix == "":
                return ""

        return prefix