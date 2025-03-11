## Leetcode - 238 [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

- **Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and without using the division operation.**

### Video Explanation: [Neetcode.io](https://youtu.be/bNvIQI2wAjk?si=EQm1ibGnIbFNOQXe)

### Additional Notes:
- use nested loop with O(n^2) complexity
- In prefix and postfix method first calculate prefix by declaring a prefix var and multiply it with every array element
- For post fix do the same, just backwards