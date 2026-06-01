# Module Resolution: ESM vs CJS Interop
## What
Module resolution refers to the process of locating and loading JavaScript modules. There are two primary module systems in JavaScript: CommonJS (CJS) and ECMAScript Modules (ESM). Understanding the differences between these two systems is crucial for effective module resolution and interop.

## Why
The main reason for using ESM over CJS is to take advantage of features like tree-shaking, which can significantly reduce bundle sizes. However, many existing libraries and frameworks are built using CJS, making interop between the two systems essential. TypeScript supports both ESM and CJS, providing a way to work with both module systems seamlessly.

## How
To achieve interop between ESM and CJS, TypeScript provides several options. One approach is to use the `--module` and `--moduleResolution` compiler options to specify the module system and resolution strategy. For example, setting `--module` to `es2020` and `--moduleResolution` to `node` allows for ESM to CJS interop.

## One exercise or command
To demonstrate ESM to CJS interop, create a new TypeScript project and add a `package.json` file with the following content:
```json
{
  "type": "module"
}
```
Then, create an ESM module `hello.mjs`:
```javascript
export function hello() {
  console.log('Hello, world!');
}
```
Next, create a CJS module `index.cjs` that imports the ESM module:
```javascript
const { hello } = await import('./hello.mjs');
hello();
```
Finally, compile and run the code using the following command:
```bash
tsc --module es2020 --moduleResolution node index.cjs && node index.cjs
```

## Further reading
* The TypeScript handbook: [Modules](https://www.typescriptlang.org/docs/handbook/modules.html)
* ECMAScript Modules: [ECMAScript specification](https://tc39.es/ecma262/#sec-modules)
* Node.js documentation: [ESM support](https://nodejs.org/api/esm.html)
* TypeScript documentation: [Module resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)

## Senior interview checkpoint

**Prompt:** Refactor an API client to discriminated unions; show how this prevents runtime bugs.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
