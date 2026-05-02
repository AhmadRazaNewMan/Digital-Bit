# Module Resolution: ESM vs CJS Interop
## What
Module resolution in JavaScript and TypeScript refers to the process of locating and loading modules. There are two types of module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses `require` and `module.exports`, while ESM uses `import` and `export`.

## Why
Understanding the differences between ESM and CJS is crucial for interoperability between the two systems. As JavaScript and TypeScript projects increasingly adopt ESM, it's essential to know how to resolve modules in both systems. This knowledge helps developers to create compatible and maintainable code.

## How
In ESM, module resolution is done using the `import` statement, which specifies the module's URL or path. The browser or Node.js resolves the module by fetching it from the specified location. In CJS, module resolution is done using the `require` function, which searches for the module in the `node_modules` directory and its subdirectories.

## One exercise or command
To demonstrate ESM and CJS interop, create a new TypeScript project with the following `tsconfig.json` configuration:
```typescript
{
  "compilerOptions": {
    "module": "ES2020",
    "moduleResolution": "node"
  }
}
```
Then, create an ESM module `greeter.mjs`:
```javascript
export function greet(name) {
  console.log(`Hello, ${name}!`);
}
```
And a CJS module `index.js` that imports the ESM module:
```javascript
const { greet } = await import('./greeter.mjs');
greet('Alice');
```
Run the command `node index.js` to see the greeting message.

## Further reading
* [ECMAScript Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
* [Node.js module documentation](https://nodejs.org/api/modules.html)
* [TypeScript module resolution documentation](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
* [ESM and CJS interop in TypeScript](https://www.typescriptlang.org/docs/handbook/esm-node.html)
