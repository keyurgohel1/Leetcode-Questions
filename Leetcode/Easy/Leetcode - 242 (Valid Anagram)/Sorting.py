class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # User this if sorted 
        # return sorted(s) == sorted(t)

        # Use this for in built functions
        return Counter(s) == Counter(t)
        