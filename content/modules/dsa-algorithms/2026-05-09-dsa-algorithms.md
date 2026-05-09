# Counting Inversions with Merge Sort Pattern
## What
Counting inversions is a process of determining the number of pairs of elements in an array that are in the wrong order, i.e., a larger element appears before a smaller element. The merge sort pattern can be utilized to count these inversions efficiently. Inversions are crucial in various data analysis and algorithmic applications, providing insight into the sortedness or disorder of a dataset.

## Why
Understanding and counting inversions are important for several reasons:
- **Data Analysis**: Inversions can indicate how sorted or unsorted a dataset is, which is useful in data preprocessing steps.
- **Algorithm Efficiency**: Some algorithms' performance can be measured or predicted based on the number of inversions in the input data.
- **Educational Tool**: Counting inversions with merge sort helps in understanding the principles of sorting algorithms and their applications beyond just sorting.

## How
To count inversions using the merge sort pattern, follow these steps:
1. **Divide**: Divide the array into two halves until each half contains one element (since a single-element array is inherently sorted).
2. **Merge and Count**: Merge these halves while counting inversions. An inversion is counted each time an element from the right half is smaller than an element from the left half, indicating they are in the wrong order.
3. **Recursion**: Apply this process recursively to each half until the entire array is merged and all inversions are counted.

## One Exercise or Command
Implement a function `count_inversions(arr)` that takes an array as input and returns the number of inversions in the array using the merge sort pattern. Start with a simple example like `arr = [1, 20, 6, 4, 5]` to see how the function works.

## Further Reading
* **Merge Sort Basics**: Review how merge sort works to better understand how inversions can be counted during the merge process.
* **Inversion Counting Applications**: Look into applications of inversion counting in data analysis and algorithm design.
* **Implementation Variations**: Explore different programming languages' implementations of inversion counting with merge sort to see how the approach can be adapted.
