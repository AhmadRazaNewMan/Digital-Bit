# Structured Logs vs Metrics vs Traces: When to Use Each
## What
Structured logs, metrics, and traces are three types of data used in monitoring and observability. Structured logs are detailed records of events, metrics provide quantitative measurements, and traces track the flow of requests through a system.

## Why
Understanding when to use each type of data is crucial for effective monitoring and debugging. Structured logs are useful for auditing and troubleshooting, metrics help with performance monitoring and alerting, and traces aid in understanding complex system interactions.

## How
- Use structured logs for error tracking, security auditing, and compliance monitoring.
- Use metrics for monitoring system performance, resource utilization, and alerting on thresholds.
- Use traces for understanding request flows, identifying bottlenecks, and optimizing system performance.

## One Exercise or Command
To get started with structured logging, try using a logging framework like Log4j or Logback to generate JSON-formatted log messages. For example, you can use the `log4j` command to configure logging levels and output formats.

## Further Reading
* Key differences between logging, metrics, and tracing: 
  * Logging: records events for auditing and debugging
  * Metrics: measures system performance and resource utilization
  * Tracing: tracks request flows and system interactions
* Best practices for implementing structured logging, metrics, and tracing in your application
* Tools and technologies for logging (e.g., ELK Stack), metrics (e.g., Prometheus), and tracing (e.g., OpenTelemetry)

## Senior interview checkpoint

**Prompt:** Design CI guardrails to prevent secret leaks and oversized images.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
