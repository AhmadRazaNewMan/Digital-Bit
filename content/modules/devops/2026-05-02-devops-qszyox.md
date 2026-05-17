# Structured Logs vs Metrics vs Traces
## What
Structured logs, metrics, and traces are three types of monitoring data used in devops to understand the performance and behavior of systems. 
- Structured logs are detailed records of events, often used for debugging and auditing.
- Metrics provide quantitative measurements, such as counts or rates, to track system performance.
- Traces show the flow of requests through a system, highlighting dependencies and latency.

## Why
Each type of data serves a different purpose and is suited for specific use cases. 
- Structured logs are ideal for troubleshooting specific issues or understanding rare events.
- Metrics are better for monitoring overall system health and performance, allowing for alerts and automation.
- Traces are useful for optimizing complex systems, identifying bottlenecks, and understanding user journeys.

## How
To decide when to use each type of data, consider the following:
- Use structured logs when debugging a specific issue or analyzing rare events.
- Use metrics for monitoring system performance, tracking key indicators, and triggering alerts.
- Use traces for understanding complex workflows, identifying performance bottlenecks, and optimizing user experiences.

## One exercise or command
Try running a command like `kubectl logs -f` to stream recent logs from a pod in a Kubernetes cluster, or use a tool like `prometheus` to collect metrics from your system, and `jaeger` to trace requests through a microservices architecture.

## Further reading
* [OpenTelemetry](https://opentelemetry.io/) for a standardized approach to tracing and metrics
* [Prometheus](https://prometheus.io/) for metric collection and alerting
* [ELK Stack](https://www.elastic.co/what-is/elk-stack) for log collection, processing, and visualization
* [Distributed Tracing](https://www.jaegertracing.io/) for understanding complex system flows
* [Monitoring and Observability](https://www.weave.works/blog/monitoring-and-observability-what-is-the-difference) to distinguish between monitoring and observability concepts in devops

## Senior interview checkpoint

**Prompt:** Draft a rollback plan for failed blue-green deployment with partial data migrations.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
