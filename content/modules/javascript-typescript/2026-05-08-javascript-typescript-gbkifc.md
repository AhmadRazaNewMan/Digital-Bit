# Narrowing with Discriminated Unions
## What
Narrowing with discriminated unions in TypeScript refers to the process of using a common, shared property (the discriminant) among union types to distinguish between them. This allows for more precise type checking and control flow analysis within code that handles these unions.

## Why
The ability to narrow types based on discriminated unions is crucial because it enables developers to write more expressive and type-safe code. By leveraging the discriminant property, developers can ensure that their code is correctly handling different members of a union type, reducing the likelihood of type-related errors at runtime.

## How
To narrow types with discriminated unions, you first define a set of types that share a common property (the discriminant). Then, within functions or conditional statements, you use type guards (like `if` statements or user-defined type guard functions) to check the discriminant property. Based on the value of the discriminant, TypeScript can infer the specific type within the union that is being handled, thus narrowing the type.

## One Exercise or Command
Consider a simple example where you have a union of two types, `Circle` and `Rectangle`, each with a `kind` property as the discriminant:
```javascript
type Shape = 
  | { kind: 'circle', radius: number }
  | { kind: 'rectangle', width: number, height: number };

function area(shape: Shape) {
  if (shape.kind === 'circle') {
    // TypeScript knows shape is { kind: 'circle', radius: number } here
    return Math.PI * shape.radius ** 2;
  } else {
    // TypeScript knows shape is { kind: 'rectangle', width: number, height: number } here
    return shape.width * shape.height;
  }
}
```

## Further Reading
* The official TypeScript documentation provides detailed information on [discriminated unions](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions) and how they can be used to create more robust and type-safe code.
* [Type Guard Functions](https://www.typescriptlang.org/docs/handbook/advanced-types.html#user-defined-type-guards) can further enhance the use of discriminated unions by allowing custom logic to narrow types.
* Articles and tutorials on [TypeScriptlang.org](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html) and other developer blogs often include examples and best practices for using discriminated unions effectively in real-world applications.

## Senior interview checkpoint

**Prompt:** Refactor an API client to discriminated unions; show how this prevents runtime bugs.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
