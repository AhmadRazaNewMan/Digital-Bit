# Narrowing with Discriminated Unions
## What
Narrowing with discriminated unions in TypeScript refers to the ability to narrow the type of a value within a specific scope, based on a common, singular discriminating property. This allows for more precise type checking and better code completion.

## Why
Discriminated unions are useful when working with complex data structures that have a common property which can be used to distinguish between different types. By using discriminated unions, developers can write more expressive and type-safe code, reducing the need for type assertions and improving code maintainability.

## How
To use narrowing with discriminated unions, you define a type that has a common property, and then create a type guard that checks the value of that property. TypeScript can then use this type guard to narrow the type of the value within a specific scope. This can be achieved using the `in` operator or by creating a custom type guard function.

## One exercise or command
Try creating a simple discriminated union in TypeScript, such as a `Rectangle` or `Circle` shape, and use a type guard to narrow the type of the shape based on its `type` property:
```javascript
type Shape = 
  | { type: 'rectangle'; width: number; height: number }
  | { type: 'circle'; radius: number }

function isRectangle(shape: Shape): shape is { type: 'rectangle'; width: number; height: number } {
  return shape.type === 'rectangle';
}

const shape: Shape = { type: 'rectangle', width: 10, height: 20 };
if (isRectangle(shape)) {
  console.log(shape.width); // shape is now known to be a rectangle
}
```

## Further reading
* The official TypeScript documentation on [discriminated unions](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)
* An article on [TypeScript type guards](https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-guards) 
* A tutorial on [using discriminated unions in TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions)
