# Rate Limiting: Token Bucket vs Leaky Bucket
## What
Rate limiting is a technique used to control the amount of traffic that an API or a system can handle within a given time frame. It helps prevent abuse, ensures fair usage, and maintains the overall performance of the system. Two popular algorithms used for rate limiting are the Token Bucket and the Leaky Bucket.

## Why
The Token Bucket and Leaky Bucket algorithms are used to limit the rate at which requests are processed. The main difference between the two lies in how they handle bursts of traffic. The Token Bucket algorithm allows for bursts by accumulating tokens over time, while the Leaky Bucket algorithm smoothes out bursts by leaking tokens at a constant rate.

## How
* Token Bucket: This algorithm uses a bucket that can hold a certain number of tokens. Tokens are added to the bucket at a constant rate, and each request consumes one token. If the bucket is empty, the request is blocked until a token is available.
* Leaky Bucket: This algorithm uses a bucket that leaks at a constant rate. Requests fill the bucket, and if the bucket is full, the request is blocked. The leak rate determines the maximum rate at which requests can be processed.

## One exercise or command
To illustrate the difference between the two algorithms, consider a simple example: a web server that allows 10 requests per minute. Using the Token Bucket algorithm, if 5 requests are made in the first second, the bucket will still have 5 tokens available for the remaining 59 seconds. Using the Leaky Bucket algorithm, if 5 requests are made in the first second, the bucket will be filled, and subsequent requests will be blocked until the bucket leaks at a rate of 1 request per 6 seconds.

## Further reading
* Token Bucket algorithm advantages:
  + Allows for bursts of traffic
  + Accumulates tokens over time
* Leaky Bucket algorithm advantages:
  + Smoothes out bursts of traffic
  + Provides a constant rate of requests
* Comparison of Token Bucket and Leaky Bucket algorithms:
  + Token Bucket is more flexible, while Leaky Bucket is more predictable
  + Token Bucket is suitable for systems with variable traffic, while Leaky Bucket is suitable for systems with constant traffic
