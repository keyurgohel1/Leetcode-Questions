## Leetcode - 347 [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

- **Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.**

### Video Explanation: [Neetcode.io](https://youtu.be/YPTqKIgVk-k?si=J1mjMGZrDuPYNCFz)

### Additional Notes:
- make a hash map first to count frequency.
- use max heap to pop out most frequent element (use to reduce time complexity)
- can use simple while loop with increased time complexity to solve the problem as well