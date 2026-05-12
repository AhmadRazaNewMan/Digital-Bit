# Validation at the Boundary: DTOs and Schemas
## What
Validation at the boundary refers to the process of verifying the correctness and consistency of data as it enters or leaves a system. In the context of backend development, this typically involves using Data Transfer Objects (DTOs) and schemas to define the structure and constraints of the data. DTOs are objects that carry data between processes, while schemas provide a blueprint for the data's organization and rules.

## Why
Validating data at the boundary is crucial for ensuring the integrity and reliability of a system. It helps to prevent common issues such as:
* Data corruption or inconsistencies
* Security vulnerabilities
* Errors in business logic
By using DTOs and schemas, developers can enforce strict data validation and guarantee that the data conforms to the expected format and rules.

## How
To implement validation at the boundary using DTOs and schemas, follow these general steps:
* Define the DTOs and their properties, including any constraints or rules
* Create schemas to describe the structure and organization of the data
* Use a validation library or framework to check the data against the schemas and DTOs
* Handle any validation errors or exceptions that occur during the process

## One exercise or command
Try using a popular validation library such as `joi` or `zod` to define a schema for a simple DTO, and then validate a sample data object against that schema. For example:
* Define a schema for a `User` DTO with properties `name` and `email`
* Create a sample data object with valid and invalid values for the `name` and `email` properties
* Use the validation library to check the sample data against the schema and handle any errors that occur

## Further reading
* Data Transfer Objects (DTOs) and their role in backend development
* Introduction to JSON Schema and its applications
* Popular validation libraries and frameworks for backend development, such as:
  + `joi`
  + `zod`
  + `ajv`
* Best practices for implementing validation at the boundary in backend systems

## Senior interview checkpoint

**Prompt:** Explain how to debug p95 latency spikes in a Node API under burst traffic.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
