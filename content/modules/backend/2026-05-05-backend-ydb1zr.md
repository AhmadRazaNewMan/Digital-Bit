# Validation at the Boundary: DTOs and Schemas
## What
Validation at the boundary refers to the process of verifying the correctness and consistency of data at the entry points of an application, typically when receiving data from external sources such as users or other services. Data Transfer Objects (DTOs) and schemas play a crucial role in this process, as they define the structure and constraints of the data being exchanged.

## Why
Validating data at the boundary is essential to ensure the reliability and security of an application. It helps prevent common web vulnerabilities such as SQL injection and cross-site scripting (XSS), and also ensures that the data being processed is consistent and accurate. By using DTOs and schemas, developers can define a clear contract for the data being exchanged, making it easier to catch errors and inconsistencies early on.

## How
To implement validation at the boundary using DTOs and schemas, developers can follow these general steps:
* Define the structure and constraints of the data using a schema definition language such as JSON Schema or Avro
* Create DTOs that conform to the defined schema
* Use a validation library or framework to check the incoming data against the schema
* Handle any validation errors that occur, such as returning an error response to the client

## One exercise or command
To get started with validation at the boundary, try creating a simple JSON Schema definition for a user registration form, and then use a validation library such as Ajv to validate incoming user data against the schema. For example:
* Define a JSON Schema for the user registration form: `{ "type": "object", "properties": { "username": { "type": "string" }, "email": { "type": "string", "format": "email" } } }`
* Use Ajv to validate incoming user data against the schema: `ajv.validate(schema, userData)`

## Further reading
* Key concepts:
  + Data Transfer Objects (DTOs)
  + Schemas and schema definition languages (e.g. JSON Schema, Avro)
  + Validation libraries and frameworks (e.g. Ajv, Joi)
* Relevant technologies:
  + API design and development
  + Web security and vulnerability prevention
  + Data modeling and validation
* Recommended resources:
  + JSON Schema documentation: https://json-schema.org/
  + Ajv documentation: https://ajv.js.org/
  + API design best practices: https://apiblueprint.org/

## Senior interview checkpoint

**Prompt:** Design idempotent retry handling for a payment callback endpoint.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
