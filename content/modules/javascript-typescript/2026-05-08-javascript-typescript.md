# Structural Typing vs Nominal Typing in TypeScript: Practical Gotchas
## What
Structural typing and nominal typing are two different approaches to type checking in TypeScript. Structural typing checks the structure of an object, including its properties and methods, to determine its type. Nominal typing, on the other hand, checks the name of the type to determine its compatibility. 

## Why
Understanding the difference between structural and nominal typing is important in TypeScript because it can help developers avoid common pitfalls and bugs. For example, when using structural typing, two objects with the same structure can be considered compatible, even if they have different type names. This can lead to unexpected behavior if not handled carefully.

## How
In TypeScript, structural typing is the default approach. This means that when you define an interface or a type, TypeScript will check the structure of the object to determine its compatibility. To use nominal typing, you need to use the `branding` technique, which involves adding a unique property to the type to distinguish it from other types.

## One exercise or command
To illustrate the difference between structural and nominal typing, consider the following example:
```javascript
interface Circle {
  radius: number;
}

interface Ellipse {
  radius: number;
}

const circle: Circle = { radius: 5 };
const ellipse: Ellipse = circle; // This is allowed because of structural typing
```
In this example, even though `circle` and `ellipse` have different type names, they are considered compatible because of their structure.

## Further reading
* TypeScript documentation on [type compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
* Article on [nominal typing in TypeScript](https://spin.atomicobject.com/2022/01/19/nominal-typing-typescript/)
* GitHub discussion on [structural vs nominal typing](https://github.com/microsoft/TypeScript/issues/202)

## Senior interview checkpoint

**Prompt:** Refactor an API client to discriminated unions; show how this prevents runtime bugs.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
