# REST vs RPC vs GraphQL — When to Choose Each
## What
REST, RPC, and GraphQL are three popular API design approaches used for building backend services. 
* REST (Representational State of Resource) is an architectural style that focuses on resources and their representations.
* RPC (Remote Procedure Call) is a protocol that allows a program to call procedures or methods on another program or computer over a network.
* GraphQL is a query language for APIs that allows clients to specify exactly what data they need.

## Why
Understanding the differences between these approaches is crucial for choosing the right one for a project. 
* REST is suitable for simple, resource-based APIs with a fixed set of endpoints.
* RPC is often used for complex, procedure-based APIs with a large number of methods.
* GraphQL is ideal for APIs with complex, changing data requirements and a need for flexible querying.

## How
When deciding between REST, RPC, and GraphQL, consider the following factors:
* Data complexity: If the data is simple and resource-based, REST might be a good choice. If the data is complex and requires flexible querying, GraphQL could be a better fit.
* API complexity: If the API has a large number of methods or procedures, RPC might be more suitable.
* Client requirements: If clients need to specify exactly what data they need, GraphQL is a good option.

## One Exercise or Command
To get started with GraphQL, try running the following command to install the GraphQL CLI tool: `npm install -g graphql-cli`

## Further Reading
* REST:
  + https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
* RPC:
  + https://en.wikipedia.org/wiki/Remote_procedure_call
* GraphQL:
  + https://graphql.org/learn/

## Senior interview checkpoint

**Prompt:** Design idempotent retry handling for a payment callback endpoint.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
