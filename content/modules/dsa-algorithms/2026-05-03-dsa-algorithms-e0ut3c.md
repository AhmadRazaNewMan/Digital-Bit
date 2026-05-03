# Sliding Window Maximum using Monotone Deque
## What
The sliding window maximum problem is a classic problem in computer science where we need to find the maximum element in a subarray of a given size. This problem can be solved efficiently using a monotone deque data structure. A monotone deque is a double-ended queue that maintains a monotonic sequence of elements, either increasing or decreasing.

## Why
The sliding window maximum problem has many real-world applications, such as finding the maximum temperature in a given time window, or the maximum stock price in a given time period. The monotone deque approach is particularly useful because it allows us to efficiently find the maximum element in a subarray without having to iterate over all elements in the subarray.

## How
To solve the sliding window maximum problem using a monotone deque, we maintain a deque of indices of the elements in the current window. The deque is maintained in such a way that the front of the deque always contains the index of the maximum element in the current window. We iterate over the array, and for each element, we remove all elements from the back of the deque that are smaller than the current element. We then add the current element to the back of the deque. When the window size is reached, we start removing elements from the front of the deque that are out of the current window.

## One exercise or command
Implement a function `sliding_window_max` that takes an array `arr` and a window size `k` as input, and returns an array of maximum elements in each window of size `k`. For example, given `arr = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[3, 3, 5, 5, 6, 7]`.

## Further reading
* The monotone deque approach is a variation of the sliding window technique, which is a common technique used in array and string problems.
* The time complexity of the monotone deque approach is O(n), where n is the size of the input array.
* The space complexity of the monotone deque approach is O(k), where k is the window size.
* Other variations of the sliding window maximum problem include finding the minimum element in a subarray, or finding the maximum or minimum element in a subarray with certain constraints.
