# Cache Stampede and Probabilistic Early Expiration
## What
Cache stampede, also known as cache thundering herd or dog-piling, occurs when multiple requests try to retrieve the same data from a cache simultaneously, resulting in a surge of requests to the underlying system. Probabilistic early expiration is a technique used to mitigate this issue by introducing randomness in the expiration time of cache entries.

## Why
Cache stampede can lead to increased latency, resource utilization, and even system crashes. By implementing probabilistic early expiration, the system can reduce the likelihood of cache stampede by staggering the expiration times of cache entries, thereby preventing multiple requests from being issued at the same time.

## How
To implement probabilistic early expiration, a random value is added to the expiration time of each cache entry. This random value is typically small compared to the overall expiration time, but sufficient to introduce enough variability to prevent cache stampede. For example, if the expiration time is set to 60 seconds, a random value between 0-10 seconds can be added to it, resulting in an expiration time between 50-70 seconds.

## One exercise or command
Try implementing a simple cache system with probabilistic early expiration using a programming language of your choice. For example, in Python, you can use the `random` library to introduce randomness in the expiration time: `expiration_time = 60 + random.randint(0, 10)`.

## Further reading
* Learn about different cache eviction policies, such as LRU, LFU, and TTL
* Understand the trade-offs between cache hit ratio, latency, and resource utilization
* Explore other techniques to mitigate cache stampede, such as cache locking and asynchronous cache refresh
* Study real-world examples of cache systems that use probabilistic early expiration, such as Redis and Memcached

## Senior interview checkpoint

**Prompt:** Design a rate limiter that supports both global and per-user quotas.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
