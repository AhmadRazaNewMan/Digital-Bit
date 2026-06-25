# Narrowing with Discriminated Unions
## What
Narrowing with discriminated unions in TypeScript is a method to narrow the type of a value within a certain scope. Discriminated unions are useful when working with union types that have a common property, known as a discriminant or tag.

## Why
The main reason to use discriminated unions is to provide more precise type checking in situations where a union type is used, but different members of the union have different properties. This is particularly useful in scenarios where you need to perform different actions based on the specific type of an object.

## How
To use discriminated unions for narrowing, you first define a union type with a common discriminant property. Then, within a specific scope, such as a function or an if statement, you use type guards or switch statements to narrow the type of a value based on its discriminant.

## One exercise or command
Try creating a simple discriminated union in TypeScript:
```typescript
type Square = { type: 'square'; side: number };
type Circle = { type: 'circle'; radius: number };
type Shape = Square | Circle;

const shape: Shape = { type: 'square', side: 10 };

if (shape.type === 'square') {
  // Within this scope, shape is narrowed to Square
  console.log(shape.side);
}
```

## Further reading
* The official TypeScript documentation on [discriminated unions](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions)
* Type guards and how they can be used for narrowing
* Using switch statements for type narrowing in TypeScript
* Advanced types and type manipulation in TypeScript for more complex scenarios

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
