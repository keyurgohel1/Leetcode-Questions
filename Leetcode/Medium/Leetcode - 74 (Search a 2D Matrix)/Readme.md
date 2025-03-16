## Leetcode - 36 [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

- **You are given an m x n integer matrix matrix with the following two properties:**

    **Each row is sorted in non-decreasing order.**
    **The first integer of each row is greater than the last integer of the previous row.**

**Given an integer target, return true if target is in matrix or false otherwise.**

**You must write a solution in O(log(m * n)) time complexity.**


### Video Explanation: [Neetcode.io](https://youtu.be/Ber2pi2C0j0?si=tIepz78MIfPJ-gZ0)

### Additional Notes:
- Better Time and Space Complexity than striver
- First do a binary search on rows
- compare highest and lowest values of rows to target and determine which row has the target value
- apply binary search on that row