# Narrowing with Discriminated Unions
## What
Narrowing with discriminated unions in TypeScript refers to the process of using a specific type of union to narrow down the type of a value within a certain scope. Discriminated unions are a powerful feature in TypeScript that allows for more expressive and type-safe code. They consist of a union of object types where each type has a common property, known as the discriminant.

## Why
The primary reason to use narrowing with discriminated unions is to leverage TypeScript's type inference capabilities to ensure type safety in complex conditional logic. By using a discriminant, TypeScript can automatically narrow the type of a value based on the value of the discriminant, allowing for more precise type checking and reducing the need for type assertions or guards.

## How
To use narrowing with discriminated unions, you define a union type where each member of the union has a common property (the discriminant) with a literal type. Then, when you use a value of that union type in a conditional statement that checks the discriminant, TypeScript will automatically narrow the type of the value to the specific member of the union that matches the condition. This can be particularly useful in functional programming patterns or when dealing with complex data structures.

## One exercise or command
Try defining a discriminated union for a simple state machine, such as a `LoadingState` or `ErrorState`, and see how TypeScript narrows the type as you handle different states:
```typescript
type State = 
  | { type: 'loading' }
  | { type: 'error', message: string }
  | { type: 'success', data: string };

function handleState(state: State) {
  if (state.type === 'error') {
    // TypeScript knows state is { type: 'error', message: string } here
    console.log(state.message);
  }
}
```

## Further reading
* The TypeScript documentation on [discriminated unions](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions) provides a comprehensive overview.
* The concept of [type guards](https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-guards) is closely related and useful for more complex scenarios.
* Looking into [pattern matching](https://github.com/microsoft/TypeScript/issues/16928) proposals and discussions can offer insight into future directions for TypeScript's type system.

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
