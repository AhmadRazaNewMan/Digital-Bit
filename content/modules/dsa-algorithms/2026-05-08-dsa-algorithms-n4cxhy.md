# Heap Applications: Median Stream and K-Way Merge
## What
Heap data structures are versatile and have numerous applications, particularly in solving problems that involve priority queuing, sorting, and median calculations. Two significant applications of heaps are in finding the median of a stream of numbers and in merging k sorted lists.

## Why
The median of a stream of numbers is a critical metric in statistics and data analysis, often used to understand the central tendency of a dataset. Heaps can efficiently calculate the median by maintaining two heaps: a max-heap for the lower half of the numbers and a min-heap for the upper half. The k-way merge problem involves merging k sorted lists into one sorted list, which is essential in databases, file systems, and other applications where data is often split and needs to be combined efficiently.

## How
To find the median of a stream using heaps, we maintain two heaps: a max-heap to store the smaller half of the numbers and a min-heap to store the larger half. For each incoming number, we add it to the appropriate heap and then balance the heaps to ensure the max-heap's size is either equal to or one greater than the min-heap's size. For the k-way merge, we use a min-heap to store the current smallest element from each list along with the list it comes from and its index in that list. We repeatedly extract the smallest element from the heap and add the next element from the same list to the heap until all elements are processed.

## One exercise or command
Implement a MedianFinder class that supports adding a number to the stream and finding the current median. Use two heaps to efficiently calculate the median after each addition.

## Further reading
* Learn about the time and space complexity of heap operations and how they apply to the median stream and k-way merge problems.
* Explore other applications of heaps, such as heap sort, priority queuing, and graph algorithms like Prim's and Kruskal's for finding minimum spanning trees.
* Study the implementation details of min-heaps and max-heaps in programming languages and libraries, focusing on how they handle edge cases and balancing.
