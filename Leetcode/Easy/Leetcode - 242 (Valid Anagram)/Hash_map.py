class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Need to make dictioaries of character frequencies for both strings
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        # Comparing the dictionaries
        if s_dict == t_dict:
            return True
        else:
            return False