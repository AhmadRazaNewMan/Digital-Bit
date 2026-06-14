# Rate Limiting: Token Bucket vs Leaky Bucket
## What
Rate limiting is a technique used to control the rate at which an API or a system can handle requests. It is used to prevent abuse, denial-of-service attacks, and to ensure fair usage of resources. Two popular algorithms for rate limiting are token bucket and leaky bucket.

## Why
The token bucket and leaky bucket algorithms are used to implement rate limiting because they provide a simple and efficient way to control the rate at which requests are processed. The token bucket algorithm is more flexible and allows for bursts of traffic, while the leaky bucket algorithm is more strict and does not allow for bursts.

## How
The token bucket algorithm works by adding tokens to a bucket at a constant rate. Each request consumes a token from the bucket. If the bucket is empty, the request is blocked until a token is added. The leaky bucket algorithm works by adding requests to a bucket at a constant rate. The bucket leaks at a constant rate, and if the bucket is full, new requests are blocked.

## One exercise or command
To implement rate limiting using the token bucket algorithm, you can use the following command: `redis> INCR token_bucket -1`, where `token_bucket` is the name of the Redis key that stores the number of tokens in the bucket. If the result is negative, the request is blocked.

## Further reading
* The token bucket algorithm is described in [RFC 3714](https://tools.ietf.org/html/rfc3714)
* The leaky bucket algorithm is described in [RFC 2697](https://tools.ietf.org/html/rfc2697)
* A comparison of the token bucket and leaky bucket algorithms can be found in [this article](https://medium.com/@saisiddhardha/token-bucket-vs-leaky-bucket-algorithms-5e2cfd8a4c9a) 
* Implementing rate limiting using Redis can be found in [the Redis documentation](https://redis.io/commands/incr)

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
