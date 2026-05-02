# Structural Typing vs Nominal Typing in TypeScript: Practical Gotchas
## What
Structural typing and nominal typing are two different approaches to type checking in programming languages. Structural typing, used by TypeScript, checks the structure of an object, including its properties and methods, to determine its type. On the other hand, nominal typing checks the name of the type to determine its type.

## Why
Understanding the differences between structural and nominal typing is crucial in TypeScript because it can lead to unexpected behavior if not handled properly. For example, two objects with the same structure but different type names will be considered the same type in structural typing, which can lead to errors if they are not intended to be interchangeable.

## How
To avoid gotchas when using structural typing in TypeScript, it's essential to be aware of the implications of this approach. Here are some tips:
* Use interfaces and type aliases to define the structure of objects and avoid using the `type` keyword with a name that implies a specific type.
* Use the `as` keyword to cast an object to a specific type when working with third-party libraries or legacy code.
* Be cautious when using the `enum` type, as it can lead to nominal typing behavior.

## One exercise or command
Try the following code to see the implications of structural typing:
```javascript
interface Point {
  x: number;
  y: number;
}

const point1: Point = { x: 1, y: 2 };
const point2 = { x: 1, y: 2 };

console.log(point1 === point2); // false
console.log(point1.x === point2.x); // true
```

## Further reading
* TypeScript documentation on [type compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
* Article on [structural typing vs nominal typing](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html#structural-type-system)
* Stack Overflow question on [differences between structural and nominal typing](https://stackoverflow.com/questions/41673657/what-is-the-difference-between-structural-and-nominal-type-systems)
