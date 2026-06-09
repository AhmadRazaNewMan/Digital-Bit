# Cache Stampede and Probabilistic Early Expiration
## What
Cache stampede occurs when multiple requests try to fetch the same data from a cache that has just expired, resulting in a surge of requests to the underlying system. Probabilistic early expiration is a technique used to prevent cache stampedes by introducing randomness in the expiration time of cache entries.

## Why
Cache stampedes can lead to increased latency, decreased throughput, and even system crashes. By using probabilistic early expiration, we can reduce the likelihood of cache stampedes and improve the overall performance and reliability of the system.

## How
To implement probabilistic early expiration, we can use a technique called "jittered" expiration, where each cache entry has a slightly randomized expiration time. This can be achieved by adding a random value to the expiration time of each cache entry. For example, if the expiration time is set to 1 hour, we can add a random value between 0 and 10 minutes to the expiration time.

## One exercise or command
Try implementing a simple cache system with probabilistic early expiration using a programming language of your choice. For example, you can use Python and the `random` library to introduce randomness in the expiration time of cache entries.

## Further reading
* Learn about cache stampedes and their effects on system performance
* Understand the concept of probabilistic early expiration and its benefits
* Explore different techniques for implementing probabilistic early expiration, such as jittered expiration and exponential backoff
* Read about real-world examples of cache stampedes and how they were mitigated using probabilistic early expiration
* Study the trade-offs between cache hit ratio, latency, and system throughput when using probabilistic early expiration

## Senior interview checkpoint

**Prompt:** Explain cache invalidation strategy for hot keys with high write rates.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
