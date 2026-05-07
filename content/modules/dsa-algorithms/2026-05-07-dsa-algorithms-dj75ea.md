# Two Pointers on Sorted Arrays and Duplicates
## What
Two pointers is a technique used in algorithms to traverse arrays or lists, typically in a sorted manner. When dealing with sorted arrays and duplicates, this technique can be particularly useful for finding or removing duplicates. It involves using two pointers that move through the array, often at different speeds, to compare or manipulate elements.

## Why
The two pointers technique is efficient for handling sorted arrays with duplicates because it allows for a single pass through the data, reducing the time complexity to O(n), where n is the number of elements in the array. This is especially beneficial when dealing with large datasets where minimizing the number of operations is crucial.

## How
The process typically starts by initializing two pointers, often at the beginning of the array. One pointer may move one step at a time, while the other moves based on certain conditions, such as when a duplicate is found. The key is in how these pointers are moved and what actions are taken when they meet or pass each other. For removing duplicates, for example, one pointer keeps track of the position where the next non-duplicate element should be placed, while the other scans the array for such elements.

## One exercise or command
Implement a function that takes a sorted array as input and returns a new array with all duplicates removed. The function should use the two pointers technique and maintain the original order of elements.

## Further reading
* The two pointers technique can be applied to various problems, including finding pairs in an array that sum to a given target.
* It's also useful in string algorithms, such as checking if two strings are anagrams of each other.
* For more complex scenarios, like dealing with rotated sorted arrays, the two pointers technique can be adapted to handle the rotation.
* LeetCode and similar platforms offer numerous problems that can be solved using the two pointers technique, providing ample practice opportunities.
