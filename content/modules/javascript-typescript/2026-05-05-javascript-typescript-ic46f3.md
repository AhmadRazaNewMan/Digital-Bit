# Narrowing with Discriminated Unions
## What
Narrowing with discriminated unions in TypeScript is a technique that allows the type system to infer a more specific type for a value within a specific scope. This is particularly useful when working with unions of object types that have a common discriminant property.

## Why
The main reason to use discriminated unions is to enable the type system to narrow the type of a value based on the discriminant property. This helps catch potential errors at compile time and ensures that the code is more type-safe.

## How
To use discriminated unions, you define a union of object types with a common discriminant property. The type system will then use the value of the discriminant property to narrow the type of the value. For example, you can define a union type with a `type` property that serves as the discriminant.

## One exercise or command
Try the following example:
```javascript
type Square = {
  type: 'square';
  side: number;
};

type Circle = {
  type: 'circle';
  radius: number;
};

type Shape = Square | Circle;

const shape: Shape = {
  type: 'square',
  side: 10,
};

if (shape.type === 'square') {
  // shape is now narrowed to Square
  console.log(shape.side);
}
```

## Further reading
* The official TypeScript documentation on [discriminated unions](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions)
* An article on [TypeScript's type narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
* A tutorial on [using discriminated unions in TypeScript](https://typescript.tv/episodes/discriminated-unions-in-typescript/)
