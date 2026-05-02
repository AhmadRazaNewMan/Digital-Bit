# Reservoir Sampling for Streaming Data
## What
Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items, where n is very large or unknown. It is particularly useful when dealing with streaming data, where the data is generated on the fly and cannot fit into memory.

## Why
The importance of reservoir sampling lies in its ability to handle streaming data efficiently. Traditional sampling methods require knowing the total number of items in advance, which is not possible with streaming data. Reservoir sampling solves this problem by maintaining a reservoir of size k, where k is the number of samples desired.

## How
The reservoir sampling algorithm works as follows:
- Initialize an empty reservoir of size k.
- For each item in the stream:
  - If the reservoir is not full, add the item to the reservoir.
  - If the reservoir is full, generate a random number between 1 and the current item number.
  - If the random number is less than or equal to k, replace a random item in the reservoir with the current item.

## One exercise or command
To test your understanding of reservoir sampling, try implementing the algorithm in your preferred programming language and test it with a stream of numbers. For example, you can use the following command in Python: `python reservoir_sampling.py < input.txt`, where `reservoir_sampling.py` is your implementation and `input.txt` is a file containing a stream of numbers.

## Further reading
* The reservoir sampling algorithm is also known as Algorithm R, and it was first described by Jeffrey Vitter in 1985.
* Reservoir sampling has many applications in data mining, machine learning, and data science.
* The algorithm can be extended to handle weighted sampling, where each item has a weight associated with it.
* Reservoir sampling can be used in conjunction with other algorithms, such as clustering and classification, to improve their performance on streaming data.
