# Rate Limiting: Token Bucket vs Leaky Bucket
## What
Rate limiting is a technique used to control the amount of traffic that is sent or received by a system within a given time period. Two popular algorithms for rate limiting are the Token Bucket algorithm and the Leaky Bucket algorithm. The Token Bucket algorithm is based on the idea of a bucket that can hold a certain number of tokens, which are added to the bucket at a constant rate. The Leaky Bucket algorithm is based on the idea of a bucket that leaks at a constant rate.

## Why
The Token Bucket algorithm is more flexible and can handle bursty traffic, while the Leaky Bucket algorithm is more strict and can prevent bursty traffic. The choice of algorithm depends on the specific requirements of the system. In general, the Token Bucket algorithm is used when the system needs to allow for some burstiness in the traffic, while the Leaky Bucket algorithm is used when the system needs to strictly enforce a constant rate.

## How
Both algorithms use a bucket to keep track of the available capacity. In the Token Bucket algorithm, tokens are added to the bucket at a constant rate, and each request consumes one token. If there are no tokens available, the request is blocked. In the Leaky Bucket algorithm, the bucket leaks at a constant rate, and each request adds to the bucket. If the bucket is full, the request is blocked.

## One exercise or command
To implement a simple Token Bucket algorithm, you can use the following command: `token_bucket = []; token_rate = 10; token_capacity = 100;` and then add tokens to the bucket at the specified rate, checking if there are enough tokens available before allowing a request.

## Further reading
* The Token Bucket algorithm is described in detail in [RFC 2697](https://tools.ietf.org/html/rfc2697)
* The Leaky Bucket algorithm is described in detail in [RFC 2698](https://tools.ietf.org/html/rfc2698)
* A comparison of the two algorithms can be found in [this paper](https://www.researchgate.net/publication/220899599_A_Comparison_of_Leaky_Bucket_and_Token_Bucket_Algorithms_for_Traffic_Shaping)
* Implementations of the algorithms can be found in [this GitHub repository](https://github.com/rg3/rate-limiting)
